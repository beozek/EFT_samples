#!/usr/bin/env python3

import ROOT

def compute_cross_sections():

    # cross sections with reference point used at generator level
    sigma_ref_0_700 = 1.842e+02   # 184.2 pb
    sigma_ref_700_900 = 2.484e+01 # 24.84 pb
    sigma_ref_900_inf = 4.525e+01 # 45.25 pb

    file_0_700_path   = "0_700.root"
    file_700_900_path = "700_900.root"
    file_900_inf_path = "900_Inf.root"

    file_0_700   = ROOT.TFile.Open(file_0_700_path)
    file_700_900 = ROOT.TFile.Open(file_700_900_path)
    file_900_inf = ROOT.TFile.Open(file_900_inf_path)
    
    # -- Mtt: 0-700
    h_sumw_ref_0_700 = file_0_700.Get("LHEMttbarAnalyzer/sumw_ref")
    h_sumw_sm_0_700  = file_0_700.Get("LHEMttbarAnalyzer/sumw_sm")
    h_sumw_eft_0_700 = file_0_700.Get("LHEMttbarAnalyzer/sumw_eft")

    # -- Mtt: 700-900
    h_sumw_ref_700_900 = file_700_900.Get("LHEMttbarAnalyzer/sumw_ref")
    h_sumw_sm_700_900  = file_700_900.Get("LHEMttbarAnalyzer/sumw_sm")
    h_sumw_eft_700_900 = file_700_900.Get("LHEMttbarAnalyzer/sumw_eft")

    # -- Mtt: 900-Inf
    h_sumw_ref_900_inf = file_900_inf.Get("LHEMttbarAnalyzer/sumw_ref")
    h_sumw_sm_900_inf  = file_900_inf.Get("LHEMttbarAnalyzer/sumw_sm")
    h_sumw_eft_900_inf = file_900_inf.Get("LHEMttbarAnalyzer/sumw_eft")

    #integrals (the total sum of weights). each has 1 entry

    SumRef_0_700 = h_sumw_ref_0_700.Integral()
    SumSM_0_700  = h_sumw_sm_0_700.Integral()
    SumEFT_0_700 = h_sumw_eft_0_700.Integral()

    SumRef_700_900 = h_sumw_ref_700_900.Integral()
    SumSM_700_900  = h_sumw_sm_700_900.Integral()
    SumEFT_700_900 = h_sumw_eft_700_900.Integral()

    SumRef_900_inf = h_sumw_ref_900_inf.Integral()
    SumSM_900_inf  = h_sumw_sm_900_inf.Integral()
    SumEFT_900_inf = h_sumw_eft_900_inf.Integral()

    #compute the SM cross section using ratio * reference_xsec.
    #    cross_section_SM = sigma_ref * (SumSM / SumRef).
    #    cross_section_EFT = sigma_ref * (SumEFT / SumRef).

    #----- Mtt 0-700 -----
    cross_sm_0_700 = sigma_ref_0_700 * (SumSM_0_700 / SumRef_0_700) if SumRef_0_700 != 0 else 0
    cross_eft_0_700 = sigma_ref_0_700 * (SumEFT_0_700 / SumRef_0_700) if SumRef_0_700 != 0 else 0

    #----- Mtt 700-900 -----
    cross_sm_700_900 = sigma_ref_700_900 * (SumSM_700_900 / SumRef_700_900) if SumRef_700_900 != 0 else 0
    cross_eft_700_900 = sigma_ref_700_900 * (SumEFT_700_900 / SumRef_700_900) if SumRef_700_900 != 0 else 0

    #----- Mtt 900-Inf -----
    cross_sm_900_inf = sigma_ref_900_inf * (SumSM_900_inf / SumRef_900_inf) if SumRef_900_inf != 0 else 0
    cross_eft_900_inf = sigma_ref_900_inf * (SumEFT_900_inf / SumRef_900_inf) if SumRef_900_inf != 0 else 0

    # 7) Print out the results
    print("\n=== CROSS SECTIONS (pb) ===\n")

    print("Mtt 0-700:")
    print("  SumRef={}, SumSM={}, SumEFT={}".format(SumRef_0_700,SumSM_0_700,SumEFT_0_700))
    print("  SM cross section:  {} pb".format(cross_sm_0_700))
    print("  EFT cross section: {} pb".format(cross_eft_0_700))

    print("\nMtt 700-900:")
    print("  SumRef={}, SumSM={}, SumEFT={}".format(SumRef_700_900,SumSM_700_900,SumEFT_700_900))
    print("  SM cross section:  {} pb".format(cross_sm_700_900))
    print("  EFT cross section: {} pb".format(cross_eft_700_900))

    print("\nMtt 900-Inf:")
    print("  SumRef={}, SumSM={}, SumEFT={}".format(SumRef_900_inf, SumSM_900_inf,SumEFT_900_inf ))
    print("  SM cross section:  {} pb".format(cross_sm_900_inf))
    print("  EFT cross section: {} pb".format(cross_eft_900_inf))


if __name__ == "__main__":
    compute_cross_sections()
