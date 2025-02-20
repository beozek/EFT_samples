#include <memory>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <regex>
#include <fstream>
#include <cmath>
#include "DataFormats/Math/interface/deltaR.h"

// CMSSW Framework Headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

// CMSSW Data Formats and Services
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// ROOT Headers
#include "TLorentzVector.h"
#include "TH1D.h"

// GenParticle
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"

class LHEMttbarAnalyzer : public edm::EDAnalyzer {
public:
  explicit LHEMttbarAnalyzer(const edm::ParameterSet&);
  ~LHEMttbarAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  void endJob() override;
  void endRun(edm::Run const& iRun, edm::EventSetup const& iSetup) override;

private:
  void analyze(const edm::Event&, const edm::EventSetup&) override;

  const reco::GenParticle* findDaughter(const reco::GenParticle* p, int pdgId);
  bool isLeptonicW(const reco::GenParticle* W, TLorentzVector &lepton, TLorentzVector &neutrino);
  bool isHadronicW(const reco::GenParticle* W, std::vector<TLorentzVector> &quarks);

  // Histograms
  TH1D* h_mttbar_;
  TH1D* h_mttbar_refpoint_;                     // Invariant mass of ttbar
  TH1D* h_mttbar_refpoint_bin50_;               // Invariant mass of ttbar

  TH1D* h_mttbar_sm_;                     // Invariant mass of ttbar
  TH1D* h_mttbar_sm_bin50_;               // Invariant mass of ttbar

  TH1D* h_mttbar_eft_;       
  TH1D* h_mttbar_eft_bin50_;       

  TH1D* h_topMass_refpoint_;
  TH1D* h_antitopMass_refpoint_;

  TH1D* h_numJets_;                    // Number of jets per event
  TH1D* h_leadingLeptonPt_;            // pT of the leading lepton from W decay
  TH1D* h_averageTopPt_;               // Average pT of the top quarks
  TH1D* h_averageTopPt_LHE_;           // Average pT of the LHE top quarks
  TH1D* h_leadingLeptonPtGeneric_;     // pT of the leading lepton (generic selection)
  TH1D* h_nleps_;                      // Number of leptons per event
  TH1D* h_ntops_;                      // Number of top quarks per selected event
  TH1D* h_topsPt_;                     // Sum of pT of the top quarks
  TH1D* h_topsPt_LHE_;                 // pT of the LHE top quarks
  TH1D* h_antitopsPt_LHE_;              // pT of the LHE antitop quarks
  TH1D* h_sumw_eft_;                        // Sum of weights
  TH1D* h_sumw_sm_;
  TH1D* h_sumw_ref_;

  edm::EDGetTokenT<LHEEventProduct> lheEventToken_;
  edm::EDGetTokenT<LHERunInfoProduct> lheRunInfoToken_;
  edm::EDGetTokenT<reco::GenJetCollection> genJetsToken_;
  edm::EDGetTokenT<reco::GenParticleCollection> genParticlesToken_;

  std::map<std::string, std::string> weightIDMap_; 

  int totalEvents_;
  int semileptonicEvents_;
  bool debug_; 
};

LHEMttbarAnalyzer::LHEMttbarAnalyzer(const edm::ParameterSet& iConfig)
    : lheEventToken_(consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"))),
      lheRunInfoToken_(consumes<LHERunInfoProduct, edm::InRun>(edm::InputTag("externalLHEProducer"))),
      genJetsToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJets"))),
      genParticlesToken_(consumes<reco::GenParticleCollection>(edm::InputTag("prunedGenParticles"))),
      totalEvents_(0),
      semileptonicEvents_(0),
      debug_(iConfig.getParameter<bool>("debug")) 
      {

  edm::Service<TFileService> fs;
  h_mttbar_ = fs->make<TH1D>("mttbar", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 200, 0, 5000);

  h_mttbar_refpoint_ = fs->make<TH1D>("mttbar_refpoint", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 200, 0, 5000);
  h_mttbar_refpoint_bin50_ = fs->make<TH1D>("mttbar_refpoint_bin50", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 100, 0, 5000);
  
  h_mttbar_sm_ = fs->make<TH1D>("mttbar_sm", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 200, 0, 10000);
  h_mttbar_sm_bin50_ = fs->make<TH1D>("mttbar_sm_bin50", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 100, 0, 10000);
  
  h_mttbar_eft_ = fs->make<TH1D>("mttbar_eft", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 200, 0, 10000);
  h_mttbar_eft_bin50_ = fs->make<TH1D>("mttbar_eft_bin50", "Invariant Mass of ttbar; m_{t#bar{t}} [GeV]; Events", 100, 0, 10000);
  
  h_topMass_refpoint_ = fs->make<TH1D>("topMass_refpoint", "Top Mass (refpoint); m_{top} [GeV]; Events", 60, 0, 1500);
  h_antitopMass_refpoint_ = fs->make<TH1D>("antitopMass_refpoint", "Antitop Mass (refpoint); m_{tbar} [GeV]; Events", 60, 0, 1500);

  h_numJets_ = fs->make<TH1D>("numJets", "Number of Jets; N_{jets}; Events", 10, 0, 10);
  h_leadingLeptonPt_ = fs->make<TH1D>("leadingLeptonPt", "Lepton p_{T}; p_{T}^{lepton} [GeV]; Events", 50, 0, 500);
  h_averageTopPt_ = fs->make<TH1D>("averageTopPt", "Average Top p_{T}; p_{T}^{top} [GeV]; Events", 60, 0, 1500);
  h_averageTopPt_LHE_ = fs->make<TH1D>("averageTopPt_LHE", "Average LHE Top p_{T}; p_{T}^{top} [GeV]; Events", 60, 0, 1500);
  h_leadingLeptonPtGeneric_ = fs->make<TH1D>("leadingLeptonPtGeneric", "Leading Lepton p_{T}; p_{T}^{lepton} [GeV]; Events", 100, 0, 500);
  h_nleps_ = fs->make<TH1D>("nleps", "Number of Leptons; N_{leps}; Events", 10, 0, 10);
  h_ntops_ = fs->make<TH1D>("ntops", "Number of Tops in Selected Events; N_{tops}; Events", 5, 0, 5);
  h_topsPt_ = fs->make<TH1D>("topsPt", "Sum of Top p_{T}; p_{T}^{tops} [GeV]; Events", 50, 0, 1000);
  h_topsPt_LHE_ = fs->make<TH1D>("topsPt_LHE", "LHE Top p_{T}; p_{T}^{tops} [GeV]; Events", 50, 0, 1000);
  h_antitopsPt_LHE_ = fs->make<TH1D>("antitopsPt_LHE", "LHE AntiTop p_{T}; p_{T}^{tops} [GeV]; Events", 50, 0, 1000);

  h_sumw_eft_ = fs->make<TH1D>("sumw_eft", "Sum of EFT weights", 1, 0, 1);
  h_sumw_sm_  = fs->make<TH1D>("sumw_sm",  "Sum of SM Weights",  1, 0, 1);
  h_sumw_ref_ = fs->make<TH1D>("sumw_ref", "Sum of REF Weights", 1, 0, 1);  
}

LHEMttbarAnalyzer::~LHEMttbarAnalyzer() {}

// endJob
void LHEMttbarAnalyzer::endJob() {
  edm::LogInfo("LHEMttbarAnalyzer") << "Total events processed: " << totalEvents_;
  edm::LogInfo("LHEMttbarAnalyzer") << "Semileptonic events: " << semileptonicEvents_;
}

// endRun
void LHEMttbarAnalyzer::endRun(edm::Run const& iRun, edm::EventSetup const& iSetup) {
  edm::Handle<LHERunInfoProduct> lheRunInfo;
  iRun.getByToken(lheRunInfoToken_, lheRunInfo);
  if (!lheRunInfo.isValid()) {
    edm::LogWarning("LHEMttbarAnalyzer") << "LHERunInfoProduct not found in endRun!";
    return;
  }

  const LHERunInfoProduct& myLHERunInfoProduct = *lheRunInfo;

  weightIDMap_.clear();

  std::regex weightRegex("<weight id=\"(\\S+)\">(.*)</weight>");

  // Iterate over the headers to extract weight IDs and descriptions
  for (auto iter = myLHERunInfoProduct.headers_begin(); iter != myLHERunInfoProduct.headers_end(); ++iter) {
    if (iter->tag() == "initrwgt") {
      for (const auto& line : iter->lines()) {
        std::smatch matches;
        if (std::regex_search(line, matches, weightRegex)) {
          std::string id = matches[1];
          std::string description = matches[2];
          weightIDMap_[id] = description;
        }
      }
    }
  }

  // for (const auto& pair : weightIDMap_) {
  //   std::cout << "Weight ID: " << pair.first << ", Description: " << pair.second << std::endl;
  // }
}

void LHEMttbarAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  totalEvents_++;
  if (debug_) std::cout << "----EVENT--- " << iEvent.id().event() << std::endl;

  //////////////////////////////////////////
  // SECTION 1: LHE Part - Calculate mttbar
  //////////////////////////////////////////

  edm::Handle<LHEEventProduct> lheEvent;
  iEvent.getByToken(lheEventToken_, lheEvent);
  if (!lheEvent.isValid()) {
    if (debug_) std::cout << "LHEEventProduct not found!\n";
    return;
  }

  //////////////////////////////////////////
  // A) Collect the weights
  //////////////////////////////////////////
  double wgt_refpoint = 1.0;
  double wgt_sm_point = 1.0;
  double wgt_eft = 1.0;

  // ID for the EFT weight
  const std::string eftWeightID = "EFTrwgt0_ctGIm_m0p936_ctGRe_m0p77_cQj38_0p944_cQj18_2p709_cQu8_0p474_cQd8_m0p91_ctj8_1p553_ctu8_m0p911_ctd8_1p778_cQj31_1p266_cQj11_0p778_cQu1_0p409_cQd1_m0p332_ctj1_m2p023_ctu1_0p08_ctd1_m1p618";

  bool foundRef   = false;
  bool foundSM    = false;
  bool foundEFT   = false;

  const auto& lheWeights = lheEvent->weights();
  for (auto &w : lheWeights) {
    const std::string &wID = w.id;
    double val = w.wgt;

    if (wID == "reference_point") {
      wgt_refpoint = val;
      foundRef = true;
    }
    else if (wID == "sm_point") {
      wgt_sm_point = val;
      foundSM = true;
    }
    else if (wID == eftWeightID) {
      wgt_eft = val;
      foundEFT = true;
    }
  }

  h_sumw_eft_->Fill(0.5, wgt_eft);
  h_sumw_sm_->Fill(0.5, wgt_sm_point);
  h_sumw_ref_->Fill(0.5, wgt_refpoint);

  if (debug_) {
    if (!foundRef)   std::cout << "reference_point weight not found!\n";
    if (!foundSM)    std::cout << "sm_point weight not found!\n";
    if (!foundEFT)   std::cout << "EFT weight not found!\n";
  }

  //////////////////////////////////////////
  // B) Find LHE top and antitop by PDG ID
  //////////////////////////////////////////
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

  // Pick the last top and antitop
  TLorentzVector topPick   = topsFound.back();   
  TLorentzVector aTopPick  = antiTopsFound.back();

  // Compute mttbar from these picks
  double mttbar = (topPick + aTopPick).M();

  // std::cout << "Found top 4-vector: pt=" << topPick.Pt() << "  mass=" << topPick.M() << std::endl;  
  // std::cout << "Found antitop: " << aTopPick.Pt() << std::endl;

  h_mttbar_refpoint_->Fill(mttbar, wgt_refpoint);
  h_mttbar_sm_->Fill(mttbar, wgt_sm_point);
  h_mttbar_eft_->Fill(mttbar, wgt_eft);

  h_mttbar_refpoint_bin50_->Fill(mttbar, wgt_refpoint);
  h_mttbar_sm_bin50_->Fill(mttbar, wgt_sm_point);
  h_mttbar_eft_bin50_->Fill(mttbar, wgt_eft);

  double massTop = topPick.M();
  double massAntiTop = aTopPick.M();

  double sumTopPt_LHE = topPick.Pt() + aTopPick.Pt();  
  double TopPt_LHE = topPick.Pt(); 
  double antiTopPt_LHE = aTopPick.Pt(); 
  double avgTopPt_LHE = 0.5 * sumTopPt_LHE;

  h_topMass_refpoint_->Fill(massTop, wgt_sm_point);
  h_antitopMass_refpoint_->Fill(massAntiTop, wgt_sm_point);

  h_averageTopPt_LHE_->Fill(avgTopPt_LHE, wgt_sm_point);
  h_topsPt_LHE_->Fill(TopPt_LHE, wgt_sm_point);
  h_antitopsPt_LHE_->Fill(antiTopPt_LHE, wgt_sm_point);
  
  //////////////////////////////////////////////
  // SECTION 2: GenParticle Part - Semileptonic
  //////////////////////////////////////////////

  edm::Handle<reco::GenParticleCollection> genParts;
  iEvent.getByToken(genParticlesToken_, genParts);
  if (!genParts.isValid()) {
    if (debug_) std::cout << "GenParticleCollection not found!" << std::endl;
    return;
  }

  // Find final-state (last copy) tops
  std::vector<const reco::GenParticle*> finalTops;
  for (const auto &gp : *genParts) {
    if (abs(gp.pdgId()) == 6 && gp.isLastCopy()) {
      finalTops.push_back(&gp);
    }
  }


  if (finalTops.size() != 2) {
    if (debug_) std::cout << "Not a ttbar event or no final tops found. finalTops size: " << finalTops.size() << std::endl;
    return;
  }
  h_ntops_->Fill(finalTops.size(), wgt_sm_point);
  
  
  if (debug_) {
    std::cout << "Found " << finalTops.size() << " final-state tops at gen level." << std::endl;
    std::cout << "Top pT: " << finalTops[0]->pt() << ", Antitop pT: " << finalTops[1]->pt() << std::endl;
  }

  auto findWDaughters = [&](const reco::GenParticle* top, const reco::GenParticle*& W, const reco::GenParticle*& b) {
    W = nullptr; 
    b = nullptr;
    for (unsigned idau = 0; idau < top->numberOfDaughters(); idau++) {
      auto dau = static_cast<const reco::GenParticle*>(top->daughter(idau));
      int pdgid = dau->pdgId();
      if (abs(pdgid) == 24) W = dau;
      else if (abs(pdgid) == 5) b = dau;
    }
  };

  auto isHadronicW = [&](const reco::GenParticle* W, std::vector<TLorentzVector> &qs)->bool {
    qs.clear();
    for (unsigned idau = 0; idau < W->numberOfDaughters(); idau++) {
      auto d = static_cast<const reco::GenParticle*>(W->daughter(idau));
      int pdgid = abs(d->pdgId());
      if (pdgid <= 5) { // quarks
        TLorentzVector q;
        q.SetPtEtaPhiM(d->pt(), d->eta(), d->phi(), d->mass());
        qs.push_back(q);
      }
    }
    return (qs.size() == 2);
  };

  auto isLeptonicW = [&](const reco::GenParticle* W, TLorentzVector &lepton, TLorentzVector &neutrino)->bool {
    const reco::GenParticle* lep = nullptr; 
    const reco::GenParticle* nu = nullptr;
    for (unsigned idau = 0; idau < W->numberOfDaughters(); idau++) {
      auto d = static_cast<const reco::GenParticle*>(W->daughter(idau));
      int pdgid = abs(d->pdgId());
      if (pdgid == 11 || pdgid == 13) lep = d;
      else if (pdgid == 12 || pdgid == 14 || pdgid == 16) nu = d;
    }
    if (lep && nu) {
      lepton.SetPtEtaPhiM(lep->pt(), lep->eta(), lep->phi(), lep->mass());
      neutrino.SetPtEtaPhiM(nu->pt(), nu->eta(), nu->phi(), nu->mass());
      return true;
    }
    return false;
  };

  const reco::GenParticle* finalTop = finalTops[0];
  const reco::GenParticle* finalAntitop = finalTops[1];

  // For each top, find W and b daughters
  const reco::GenParticle *W1=nullptr, *b1=nullptr;
  const reco::GenParticle *W2=nullptr, *b2=nullptr;

  findWDaughters(finalTop, W1, b1);
  findWDaughters(finalAntitop, W2, b2);

  if (debug_) {
    std::cout << "W1 found: " << (W1!=nullptr) << ", b1 found: " << (b1!=nullptr) << std::endl;
    std::cout << "W2 found: " << (W2!=nullptr) << ", b2 found: " << (b2!=nullptr) << std::endl;
  }

  if (!W1 || !b1 || !W2 || !b2) {
    if (debug_) std::cout << "Missing W or b for one of the tops." << std::endl;
    return;
  }

  TLorentzVector wl, wnu;
  std::vector<TLorentzVector> wq;
  bool W1lept = isLeptonicW(W1, wl, wnu);
  bool W1had = (!W1lept && isHadronicW(W1, wq));
  bool W2lept = false, W2had = false;

  if (W1lept && isHadronicW(W2, wq)) W2had = true;
  else if (W1had && isLeptonicW(W2, wl, wnu)) W2lept = true;
  
  if (debug_) {
    std::cout << "W1 lept: " << W1lept << ", W1 had: " << W1had << std::endl;
    std::cout << "W2 lept: " << W2lept << ", W2 had: " << W2had << std::endl;
  }

  if (!((W1lept && W2had) || (W2lept && W1had))) {
    if (debug_) std::cout << "Not semileptonic decay." << std::endl;
    return;
  }

  // Semileptonic selection passed
  semileptonicEvents_++;
  if (debug_) std::cout << "Semileptonic condition passed." << std::endl;

  // Fill top kinematics now from GEN
  double genTopPtSum = finalTop->pt() + finalAntitop->pt();
  double genTopPtAvg = genTopPtSum / 2.0;
  h_averageTopPt_->Fill(genTopPtAvg, wgt_sm_point);
  h_topsPt_->Fill(genTopPtSum, wgt_sm_point);

  if (W2lept && W1had) {
    TLorentzVector lepton2, nu2;
    isLeptonicW(W2, lepton2, nu2);
    wl = lepton2;
    wnu = nu2;
  }

  if (debug_) std::cout << "Leptonic W lepton pT: " << wl.Pt() << ", eta: " << wl.Eta() << std::endl;
  
  // Apply lepton pT/eta cuts
  if (wl.Pt() > 20.0 && fabs(wl.Eta()) < 2.5) {
    h_leadingLeptonPt_->Fill(wl.Pt(), wgt_sm_point);
  } else {
    // If lepton doesn't pass selection, we stop here
        if (debug_) std::cout << "Lepton fails pT/eta cuts." << std::endl;
    return;
  }

  // Generic lepton selection
  std::vector<TLorentzVector> candidateLeps;
  for (const auto &gp : *genParts) {
    int pdgId = abs(gp.pdgId());
    if ((pdgId == 11 || pdgId == 13) && gp.pt() > 20.0 && fabs(gp.eta()) < 2.5) {
      TLorentzVector lepVec;
      lepVec.SetPtEtaPhiM(gp.pt(), gp.eta(), gp.phi(), gp.mass());
      candidateLeps.push_back(lepVec);
    }
  }

  int nleps = (int)candidateLeps.size();
  h_nleps_->Fill(nleps, wgt_sm_point);
  if (debug_) std::cout << "Number of candidate leptons: " << nleps << std::endl;

  if (!candidateLeps.empty()) {
    std::sort(candidateLeps.begin(), candidateLeps.end(), [](const TLorentzVector &a, const TLorentzVector &b){
      return a.Pt() > b.Pt();
    });
    TLorentzVector genericLeadingLepton = candidateLeps[0];
    h_leadingLeptonPtGeneric_->Fill(genericLeadingLepton.Pt(), wgt_sm_point);

    if (debug_) std::cout << "Generic leading lepton pT: " << genericLeadingLepton.Pt() << std::endl;
  }

  // JETS: from slimmedGenJets
  edm::Handle<reco::GenJetCollection> genJetsHandle;
  iEvent.getByToken(genJetsToken_, genJetsHandle);
  if (!genJetsHandle.isValid()) {
    if (debug_) std::cout << "GenJet collection not found!" << std::endl;
    h_numJets_->Fill(0.0, wgt_sm_point);
    return;
  }

  std::vector<const reco::GenJet*> selectedJets;
  for (const auto &jet : *genJetsHandle) {
    if (jet.pt() > 30.0 && fabs(jet.eta()) < 2.5) {
      selectedJets.push_back(&jet);
    }
  }

  if (debug_) std::cout << "Selected Jets before cleaning: " << selectedJets.size() << std::endl;

  double drmin = 0.4;
  std::vector<const reco::GenJet*> cleanJets;
  for (const auto jet : selectedJets) {
    double dR_lep = reco::deltaR(jet->eta(), jet->phi(), wl.Eta(), wl.Phi());
    if (dR_lep > drmin) {
      cleanJets.push_back(jet);
    }
  }

  int njets = (int)cleanJets.size();
  h_numJets_->Fill(njets, wgt_sm_point);

  if (debug_) {
    std::cout << "Clean jets after lepton cleaning: " << njets << std::endl;
  }
}

const reco::GenParticle* LHEMttbarAnalyzer::findDaughter(const reco::GenParticle* p, int pdgId) {
  for (unsigned i = 0; i < p->numberOfDaughters(); i++) {
    auto d = static_cast<const reco::GenParticle*>(p->daughter(i));
    if (d->pdgId() == pdgId) return d;
  }
  return nullptr;
}

void LHEMttbarAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("lheSrc", edm::InputTag("externalLHEProducer"));
  desc.add<edm::InputTag>("genJets", edm::InputTag("slimmedGenJets"));
  desc.add<edm::InputTag>("genParticles", edm::InputTag("prunedGenParticles"));
  desc.add<bool>("debug", false);
  descriptions.add("LHEMttbarAnalyzer", desc);
}

bool LHEMttbarAnalyzer::isLeptonicW(const reco::GenParticle* W, TLorentzVector &lepton, TLorentzVector &neutrino) {
  const reco::GenParticle* lep = nullptr; 
  const reco::GenParticle* nu = nullptr;
  for (unsigned idau = 0; idau < W->numberOfDaughters(); idau++) {
    auto d = static_cast<const reco::GenParticle*>(W->daughter(idau));
    int pdgid = abs(d->pdgId());
    if (pdgid == 11 || pdgid == 13) lep = d;
    else if (pdgid == 12 || pdgid == 14 || pdgid == 16) nu = d;
  }
  if (lep && nu) {
    lepton.SetPtEtaPhiM(lep->pt(), lep->eta(), lep->phi(), lep->mass());
    neutrino.SetPtEtaPhiM(nu->pt(), nu->eta(), nu->phi(), nu->mass());
    return true;
  }
  return false;
}

bool LHEMttbarAnalyzer::isHadronicW(const reco::GenParticle* W, std::vector<TLorentzVector> &qs) {
  qs.clear();
  for (unsigned idau = 0; idau < W->numberOfDaughters(); idau++) {
    auto d = static_cast<const reco::GenParticle*>(W->daughter(idau));
    int pdgid = abs(d->pdgId());
    if (pdgid <= 5) {
      TLorentzVector q;
      q.SetPtEtaPhiM(d->pt(), d->eta(), d->phi(), d->mass());
      qs.push_back(q);
    }
  }
  return (qs.size() == 2);
}

// Define as plug-in
DEFINE_FWK_MODULE(LHEMttbarAnalyzer);
