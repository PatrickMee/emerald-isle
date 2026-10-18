using System;
using EmeraldIsle;

internal static class HearthSocialEligibilityTests
{
    private static void Expect(bool actual, bool expected, string label)
    {
        if (actual != expected)
            throw new Exception(label);
    }

    private static int Main()
    {
        Expect(HearthSocialEligibility.JoyGainFactor == 1.2f, true, "joy factor");
        Expect(HearthSocialEligibility.IsHearthReady(true, true, true, true), true, "ready hearth");

        for (int missing = 0; missing < 4; missing++)
        {
            bool[] gates = { true, true, true, true };
            gates[missing] = false;
            Expect(HearthSocialEligibility.IsHearthReady(gates[0], gates[1], gates[2], gates[3]),
                false, "missing hearth/gather/fuel gate " + missing);
        }

        Expect(HearthSocialEligibility.CanApplyBonus(true, true, true, true, true, true, false),
            true, "seated valid use");
        for (int missing = 0; missing < 6; missing++)
        {
            bool[] gates = { true, true, true, true, true, true };
            gates[missing] = false;
            Expect(HearthSocialEligibility.CanApplyBonus(
                gates[0], gates[1], gates[2], gates[3], gates[4], gates[5], false),
                false, "missing bonus gate " + missing);
        }
        Expect(HearthSocialEligibility.CanApplyBonus(true, true, true, true, true, true, true),
            false, "seat blocks cooking interaction cell");
        return 0;
    }
}
