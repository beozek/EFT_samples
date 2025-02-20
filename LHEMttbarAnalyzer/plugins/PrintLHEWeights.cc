// PrintLHEWeights.cc
#include <iostream>
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

class PrintLHEWeights : public edm::EDAnalyzer {
public:
  explicit PrintLHEWeights(const edm::ParameterSet& ps)
      : lheToken_(consumes<LHEEventProduct>(ps.getParameter<edm::InputTag>("lheSrc"))) {}
  ~PrintLHEWeights() override {}

  void analyze(const edm::Event& event, const edm::EventSetup& setup) override {
    edm::Handle<LHEEventProduct> lheHandle;
    event.getByToken(lheToken_, lheHandle);
    if (lheHandle.isValid()) {
      std::cout << "Event " << event.id().event() << " has " 
                << lheHandle->weights().size() << " weights:" << std::endl;
      for (const auto& w : lheHandle->weights()) {
        std::cout << "   Weight ID: " << w.id 
                  << ", Weight value: " << w.wgt << std::endl;
      }
    } else {
      std::cout << "LHEEventProduct not found in event " << event.id().event() << std::endl;
    }
  }

private:
  edm::EDGetTokenT<LHEEventProduct> lheToken_;
};

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PrintLHEWeights);

