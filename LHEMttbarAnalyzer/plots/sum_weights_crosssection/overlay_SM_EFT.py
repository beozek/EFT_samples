import ROOT
import numpy as np
from array import array

def overlay_sm_eft():
    ROOT.gROOT.SetBatch(True) 
    ROOT.gStyle.SetOptStat(0)

    # --- The three sub-bin root files for the *SM* weights
    sm_file_1 = ROOT.TFile.Open("0_700.root")
    sm_file_2 = ROOT.TFile.Open("700_900.root")
    sm_file_3 = ROOT.TFile.Open("900_Inf.root")

    # --- The three sub-bin root files for the *EFT* weights
    eft_file_1 = ROOT.TFile.Open("0_700.root")
    eft_file_2 = ROOT.TFile.Open("700_900.root")
    eft_file_3 = ROOT.TFile.Open("900_Inf.root")

    # Simple checks for validity
    if not sm_file_1 or sm_file_1.IsZombie():
        print("Error: sm_file_1 not found or corrupted.")
        return
    if not sm_file_2 or sm_file_2.IsZombie():
        print("Error: sm_file_2 not found or corrupted.")
        return
    if not sm_file_3 or sm_file_3.IsZombie():
        print("Error: sm_file_3 not found or corrupted.")
        return

    if not eft_file_1 or eft_file_1.IsZombie():
        print("Error: eft_file_1 not found or corrupted.")
        return
    if not eft_file_2 or eft_file_2.IsZombie():
        print("Error: eft_file_2 not found or corrupted.")
        return
    if not eft_file_3 or eft_file_3.IsZombie():
        print("Error: eft_file_3 not found or corrupted.")
        return

    # --- Retrieve the mttbar histograms for each sub bin (SM)
    sm_hist_1 = sm_file_1.Get("LHEMttbarAnalyzer/mttbar_sm").Clone("sm_hist_1")
    sm_hist_2 = sm_file_2.Get("LHEMttbarAnalyzer/mttbar_sm").Clone("sm_hist_2")
    sm_hist_3 = sm_file_3.Get("LHEMttbarAnalyzer/mttbar_sm").Clone("sm_hist_3")

    # --- Retrieve the mttbar histograms for each sub bin (EFT)
    eft_hist_1 = eft_file_1.Get("LHEMttbarAnalyzer/mttbar_eft").Clone("eft_hist_1")
    eft_hist_2 = eft_file_2.Get("LHEMttbarAnalyzer/mttbar_eft").Clone("eft_hist_2")
    eft_hist_3 = eft_file_3.Get("LHEMttbarAnalyzer/mttbar_eft").Clone("eft_hist_3")

    if not sm_hist_1 or not sm_hist_2 or not sm_hist_3:
        print("Error: One SM histogram is missing.")
        return
    if not eft_hist_1 or not eft_hist_2 or not eft_hist_3:
        print("Error: One EFT histogram is missing.")
        return

    # ================================
    # Choose cross sections for each sub range, for SM *and* EFT.
    # If each sub-range has a known cross section, define it here.
    # ================================

    # Example SM cross sections in each MTT bin
    sm_sigma_0_700  = 135.062
    sm_sigma_700_900= 12.888
    sm_sigma_900_inf= 6.795

    # Example EFT cross sections in each MTT bin
    # (You will have to figure these out from your generator or from
    #  integral scans of your EFT weights, etc.)
    eft_sigma_0_700   = 140.3
    eft_sigma_700_900 = 13.7
    eft_sigma_900_inf = 7.2

    # Retrieve the sum of weights from the histograms
    # (the `GetSumOfWeights()` is the integral of that histogram)
    sm_N1 = sm_hist_1.GetSumOfWeights()
    sm_N2 = sm_hist_2.GetSumOfWeights()
    sm_N3 = sm_hist_3.GetSumOfWeights()

    eft_N1 = eft_hist_1.GetSumOfWeights()
    eft_N2 = eft_hist_2.GetSumOfWeights()
    eft_N3 = eft_hist_3.GetSumOfWeights()

    # Basic checks
    if sm_N1 == 0 or sm_N2 == 0 or sm_N3 == 0:
        print("Error: One SM sum of weights is zero.")
        return
    if eft_N1 == 0 or eft_N2 == 0 or eft_N3 == 0:
        print("Error: One EFT sum of weights is zero.")
        return

    sm_scale1 = sm_sigma_0_700   / sm_N1
    sm_scale2 = sm_sigma_700_900 / sm_N2
    sm_scale3 = sm_sigma_900_inf / sm_N3

    eft_scale1 = eft_sigma_0_700   / eft_N1
    eft_scale2 = eft_sigma_700_900 / eft_N2
    eft_scale3 = eft_sigma_900_inf / eft_N3

    print("SM scale factors: 0-700={}, 700-900={}, 900+={}".format(sm_scale1, sm_scale2, sm_scale3 ))
    print("EFT scale factors: 0-700={}, 700-900={}, 900+={}".format(eft_scale1, eft_scale2,eft_scale3 ))

    sm_hist_1.Scale(sm_scale1)
    sm_hist_2.Scale(sm_scale2)
    sm_hist_3.Scale(sm_scale3)

    eft_hist_1.Scale(eft_scale1)
    eft_hist_2.Scale(eft_scale2)
    eft_hist_3.Scale(eft_scale3)

    bin_width   = 50
    mttbar_min  = 0
    mttbar_max  = 2000
    n_bins      = int((mttbar_max - mttbar_min) / bin_width)
    bin_edges   = np.linspace(mttbar_min, mttbar_max, n_bins + 1)
    bin_edges_c = array('d', bin_edges)

    sm_1_reb = sm_hist_1.Rebin(n_bins, "sm_1_reb", bin_edges_c)
    sm_2_reb = sm_hist_2.Rebin(n_bins, "sm_2_reb", bin_edges_c)
    sm_3_reb = sm_hist_3.Rebin(n_bins, "sm_3_reb", bin_edges_c)

    eft_1_reb = eft_hist_1.Rebin(n_bins, "eft_1_reb", bin_edges_c)
    eft_2_reb = eft_hist_2.Rebin(n_bins, "eft_2_reb", bin_edges_c)
    eft_3_reb = eft_hist_3.Rebin(n_bins, "eft_3_reb", bin_edges_c)

    # Combine sub-ranges to get a single SM histogram and a single EFT histogram
    sm_combined  = sm_1_reb.Clone("sm_combined")
    sm_combined.Add(sm_2_reb)
    sm_combined.Add(sm_3_reb)

    eft_combined = eft_1_reb.Clone("eft_combined")
    eft_combined.Add(eft_2_reb)
    eft_combined.Add(eft_3_reb)

    # Basic styling
    sm_combined.SetLineColor(ROOT.kBlue)
    sm_combined.SetLineWidth(2)
    eft_combined.SetLineColor(ROOT.kRed)
    eft_combined.SetLineWidth(2)

    # Create a canvas for overlay
    c1 = ROOT.TCanvas("c1","SM vs EFT Mttbar Overlay",800,600)
    c1.SetGrid()

    # Optional: find max so they both can be drawn nicely
    max_y = max(sm_combined.GetMaximum(), eft_combined.GetMaximum())
    sm_combined.SetMaximum(max_y * 1.2)

    # Draw
    sm_combined.GetXaxis().SetTitle("m_{t#bar{t}} [GeV]")
    sm_combined.GetYaxis().SetTitle("Events (scaled by cross section)")
    sm_combined.Draw("HIST")
    eft_combined.Draw("HIST SAME")

    legend = ROOT.TLegend(0.65, 0.65, 0.88, 0.8)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.AddEntry(sm_combined,  "SM (combined bins)",  "l")
    legend.AddEntry(eft_combined, "EFT (combined bins)", "l")
    legend.Draw()

    c1.SaveAs("mttbar_overlay_sm_vs_eft.png")

    # Close the files
    sm_file_1.Close()
    sm_file_2.Close()
    sm_file_3.Close()
    eft_file_1.Close()
    eft_file_2.Close()
    eft_file_3.Close()

if __name__ == "__main__":
    overlay_sm_eft()
