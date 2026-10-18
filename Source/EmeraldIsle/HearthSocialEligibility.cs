namespace EmeraldIsle
{
    internal static class HearthSocialEligibility
    {
        internal const float JoyGainFactor = 1.2f;

        internal static bool IsHearthReady(
            bool isHearth, bool isSpawned, bool gatheringActive, bool hasFuel)
        {
            return isHearth && isSpawned && gatheringActive && hasFuel;
        }

        internal static bool CanApplyBonus(
            bool isHearth,
            bool isSpawned,
            bool gatheringActive,
            bool hasFuel,
            bool hasValidSeat,
            bool isSeated,
            bool seatBlocksCooking)
        {
            return IsHearthReady(isHearth, isSpawned, gatheringActive, hasFuel) &&
                hasValidSeat && isSeated && !seatBlocksCooking;
        }
    }
}
