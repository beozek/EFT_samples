import ROOT
from array import array
import numpy as np

def zero_bins_above(hist, cutoff=1500.0):
    """
    Zero out all histogram bins above `cutoff`.
    Returns the integral over [lowestBin, bin_cutoff].
    """
    nbins = hist.GetNbinsX()
    bin_cut = hist.FindBin(cutoff)  # The bin that includes 'cutoff'
    # Zero out bins above bin_cut
    for b in range(bin_cut+1, nbins+2):  # +1 for the next bin, +2 for overflow
        hist.SetBinContent(b, 0.0)
        hist.SetBinError(b, 0.0)
    return hist.Integral(1, nbins)

def overlay_histograms_normalized():
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)

    # Open your 3 files (0-700, 700-900, 900-inf)
    # file1 = ROOT.TFile.Open("0_700.root")
    # file2 = ROOT.TFile.Open("700_900.root")
    # file3 = ROOT.TFile.Open("900_Inf.root")


    file1 = ROOT.TFile.Open("../0_700_root/lhe_0_700.root")
    file2 = ROOT.TFile.Open("../700_900_root/lhe_700_900.root")
    file3 = ROOT.TFile.Open("../900_Inf_root/lhe_900Inf.root")

    if not file1 or file1.IsZombie():
        print("Error: Cannot open file1.")
        return
    if not file2 or file2.IsZombie():
        print("Error: Cannot open file2.")
        return
    if not file3 or file3.IsZombie():
        print("Error: Cannot open file3.")
        return

    # For instance, let's get "mttbar_eft" from each file
    hist1 = file1.Get("LHEMttbarAnalyzer/mttbar").Clone("hist1")
    hist2 = file2.Get("LHEMttbarAnalyzer/mttbar").Clone("hist2")
    hist3 = file3.Get("LHEMttbarAnalyzer/mttbar").Clone("hist3")

    if not hist1:
        print("Error: 'mttbar_eft' not found in file1.")
        return
    if not hist2:
        print("Error: 'mttbar_eft' not found in file2.")
        return
    if not hist3:
        print("Error: 'mttbar_eft' not found in file3.")
        return

    # Partial cross sections or total for each bin:
    sigma1 = 1.842e+02  # 0-700 cross section
    sigma2 = 2.484e+01  # 700-900 cross section
    sigma3 = 4.525e+01  # 900-inf cross section

    # 1) For hist1 (0-700), use full integral
    N_gen1 = hist1.GetSumOfWeights()

    # 2) For hist2 (700-900), use full integral
    N_gen2 = hist2.GetSumOfWeights()

    # 3) For hist3 (900-inf), we only want to consider up to 1500,
    #    so let's zero out bins above 1500, then take that integral as N_gen3
    N_gen3 = zero_bins_above(hist3, cutoff=1500.0)

    if N_gen1 <= 0 or N_gen2 <= 0 or N_gen3 <= 0:
        print("Error: One of the histograms has zero or negative sum of weights.")
        return

    # Now do the scale factor = sigma / N_gen
    scale1 = sigma1 / N_gen1
    scale2 = sigma2 / N_gen2
    scale3 = sigma3 / N_gen3

    print("Scale for 0-700:", scale1)
    print("Scale for 700-900:", scale2)
    print("Scale for 900-inf (only up to mtt=1500):", scale3)

    hist1.Scale(scale1)
    hist2.Scale(scale2)
    hist3.Scale(scale3)

    # Optional rebin
    bin_width = 50
    mttbar_min = 0
    mttbar_max = 1500
    n_bins = int((mttbar_max - mttbar_min)/bin_width)
    bin_edges = np.linspace(mttbar_min, mttbar_max, n_bins + 1)
    bin_edges_c = array('d', bin_edges)

    hist1r = hist1.Rebin(n_bins, "hist1_rebinned", bin_edges_c)
    hist2r = hist2.Rebin(n_bins, "hist2_rebinned", bin_edges_c)
    hist3r = hist3.Rebin(n_bins, "hist3_rebinned", bin_edges_c)

    # Combine them
    hist_combined = hist1r.Clone("hist_combined")
    hist_combined.Add(hist2r)
    hist_combined.Add(hist3r)

    c1 = ROOT.TCanvas("c1","",800,600)
    c1.SetGrid()

    # Overdraw them
    hist1r.SetLineColor(ROOT.kRed)
    hist2r.SetLineColor(ROOT.kGreen+2)
    hist3r.SetLineColor(ROOT.kBlue)
    hist_combined.SetLineColor(ROOT.kMagenta)

    hist1r.SetLineWidth(2)
    hist2r.SetLineWidth(2)
    hist3r.SetLineWidth(2)
    hist_combined.SetLineWidth(2)

    hist1r.SetStats(0)
    hist2r.SetStats(0)
    hist3r.SetStats(0)
    hist_combined.SetStats(0)

    # Draw
    hist1r.Draw("HIST")
    hist2r.Draw("HIST SAME")
    hist3r.Draw("HIST SAME")

    legend = ROOT.TLegend(0.65,0.75,0.88,0.88)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.AddEntry(hist1r, "0-700 bin","l")
    legend.AddEntry(hist2r, "700-900 bin","l")
    legend.AddEntry(hist3r, "900-inf bin (1500)","l")
    legend.Draw()

    c1.SaveAs("mttbar_overlay_1500_old.png")
    c1.Clear()

    # Optionally draw the combined
    hist_combined.Draw("HIST")
    c1.SaveAs("mttbar_combined_1500_old.png")

    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    overlay_histograms_normalized()
