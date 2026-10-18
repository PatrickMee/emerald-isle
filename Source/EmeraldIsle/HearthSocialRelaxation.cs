using System.Collections.Generic;
using RimWorld;
using Verse;
using Verse.AI;

namespace EmeraldIsle
{
    internal static class HearthSocialRelaxation
    {
        private const string HearthDefName = "EI_CentralHearth";
        private const float NativeSocialSeatRadius = 3.9f;

        internal static bool IsReady(Building hearth)
        {
            CompGatherSpot gather = hearth?.GetComp<CompGatherSpot>();
            CompRefuelable fuel = hearth?.GetComp<CompRefuelable>();
            // RimWorld's CompFireOverlay and refuelable glower both use HasFuel
            // for this building. HasFuel also accounts for its vacuum setting.
            return HearthSocialEligibility.IsHearthReady(
                hearth?.def?.defName == HearthDefName,
                hearth != null && hearth.Spawned,
                gather != null && gather.Active,
                fuel != null && fuel.HasFuel && FlickUtility.WantsToBeOn(hearth));
        }

        internal static bool HasValidSeat(Pawn pawn, Job job, Building hearth, bool seated)
        {
            if (pawn == null || job == null || hearth == null || pawn.Map != hearth.Map)
                return false;

            // Native SocialRelax changes target B from the chair to the reserved
            // sitting cell when the job begins. Resolve that cell on every tick so
            // save/reload and a removed chair cannot retain the bonus.
            IntVec3 seatCell = job.targetB.Cell;
            if (!seatCell.IsValid || !seatCell.InBounds(pawn.Map))
                return false;
            Building seat = seatCell.GetEdifice(pawn.Map);
            bool validSeat = seat != null && seat.Spawned && seat.def.building != null &&
                seat.def.building.isSittable &&
                seatCell.InHorDistOf(hearth.Position, NativeSocialSeatRadius);
            return HearthSocialEligibility.CanApplyBonus(
                hearth.def.defName == HearthDefName,
                hearth.Spawned,
                hearth.GetComp<CompGatherSpot>()?.Active == true,
                hearth.GetComp<CompRefuelable>()?.HasFuel == true,
                validSeat,
                seated && pawn.Position == seatCell,
                seatCell == hearth.InteractionCell);
        }

        internal static bool IsCandidateSeat(Job job, Building hearth)
        {
            return job != null && job.targetA.Thing == hearth &&
                job.targetB.HasThing && job.targetB.Thing is Building seat &&
                seat.def.building != null && seat.def.building.isSittable &&
                // A multi-cell bench can assign any occupied cell to the pawn.
                // Reject the whole seat if one could block the cooking position.
                !GenAdj.OccupiedRect(seat).Contains(hearth.InteractionCell);
        }
    }

    public sealed class EI_JoyGiver_HearthSocialRelax : JoyGiver_SocialRelax
    {
        public override Job TryGiveJob(Pawn pawn)
        {
            if (pawn?.Map == null)
                return null;

            // Native selection retains reachability, seat assignment, drink policy,
            // and ordinary Social joy rules. Radius zero restricts it to this hearth.
            List<CompGatherSpot> spots = pawn.Map.gatherSpotLister.activeSpots;
            if (spots.Count == 0)
                return null;
            int start = Rand.Range(0, spots.Count);
            for (int offset = 0; offset < spots.Count; offset++)
            {
                int i = (start + offset) % spots.Count;
                Building hearth = spots[i]?.parent as Building;
                if (!HearthSocialRelaxation.IsReady(hearth))
                    continue;

                Job job = base.TryGiveJobInGatheringArea(pawn, hearth.Position, 0f);
                if (HearthSocialRelaxation.IsCandidateSeat(job, hearth))
                    return job;
            }
            return null;
        }

        public override Job TryGiveJobInGatheringArea(Pawn pawn, IntVec3 gatheringSpot,
            float maxRadius = -1f)
        {
            // Party/ceremony callers use this entry point for arbitrary gathering
            // areas. Native SocialRelax still serves them without our custom job.
            return null;
        }
    }

    public sealed class EI_JobDriver_HearthSocialRelax : JobDriver_SocialRelax
    {
        protected override IEnumerable<Toil> MakeNewToils()
        {
            foreach (Toil toil in base.MakeNewToils())
            {
                // The native social-relax toil owns seating, conversation and
                // optional ingestion. Only its joy tick needs a hearth factor.
                if (toil.socialMode == RandomSocialMode.SuperActive &&
                    toil.defaultCompleteMode == ToilCompleteMode.Delay &&
                    toil.defaultDuration == job.def.joyDuration)
                    toil.tickIntervalAction = HearthJoyTick;
                yield return toil;
            }
        }

        private void HearthJoyTick(int delta)
        {
            Building hearth = job.targetA.Thing as Building;
            if (!HearthSocialRelaxation.IsReady(hearth) ||
                !HearthSocialRelaxation.HasValidSeat(pawn, job, hearth, true))
            {
                EndJobWith(JobCondition.Incompletable);
                return;
            }

            pawn.rotationTracker.FaceCell(GenAdj.OccupiedRect(hearth).ClosestCellTo(pawn.Position));
            PawnUtility.GainComfortFromCellIfPossible(pawn, delta, false);
            JoyUtility.JoyTickCheckEnd(pawn, delta, JoyTickFullJoyAction.GoToNextToil,
                HearthSocialEligibility.JoyGainFactor, null);
        }
    }
}
