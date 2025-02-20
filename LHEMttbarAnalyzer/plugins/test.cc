// Access the LHE info
const auto& hepeup = lheEvent->hepeup();
const auto& pup   = hepeup.PUP;   // 4-vectors
const auto& idup  = hepeup.IDUP;  // PDG IDs

std::vector<TLorentzVector> topsFound, antiTopsFound;

// Loop over LHE particles
for (size_t i = 0; i < idup.size(); i++) {
  int pdgId = idup[i];
  if (pdgId == 6) {
    TLorentzVector t;
    t.SetPxPyPzE(pup[i][0], pup[i][1], pup[i][2], pup[i][3]);
    topsFound.push_back(t);
  } 
  else if (pdgId == -6) {
    TLorentzVector tbar;
    tbar.SetPxPyPzE(pup[i][0], pup[i][1], pup[i][2], pup[i][3]);
    antiTopsFound.push_back(tbar);
  }
}

if (topsFound.empty() || antiTopsFound.empty()) {
  if (debug_) std::cout << "Did not find both top and antitop in LHE.\n";
  return;
}

// Pick the last top and last antitop
TLorentzVector topPick   = topsFound.back();
TLorentzVector aTopPick  = antiTopsFound.back();

// Compute mttbar from these picks
double mttbar = (topPick + aTopPick).M();

// Fill your histograms with the chosen weights
h_mttbar_refpoint_->Fill(mttbar, wgt_refpoint);
h_mttbar_sm_->Fill(mttbar, wgt_sm_point);
h_mttbar_eft_->Fill(mttbar, wgt_eft);

h_mttbar_refpoint_bin50_->Fill(mttbar, wgt_refpoint);
h_mttbar_sm_bin50_->Fill(mttbar, wgt_sm_point);
h_mttbar_eft_bin50_->Fill(mttbar, wgt_eft);

// If you want the individual top masses/pT:
double massTop = topPick.M();
double massAntiTop = aTopPick.M();
double sumTopPt_LHE = topPick.Pt() + aTopPick.Pt();
double avgTopPt_LHE = 0.5 * sumTopPt_LHE;

// Fill top mass histograms (assuming you declared them)
h_topMass_refpoint_->Fill(massTop, wgt_refpoint);
h_antitopMass_refpoint_->Fill(massAntiTop, wgt_refpoint);

// Fill top pT histograms, etc.
