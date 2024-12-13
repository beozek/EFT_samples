import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

# Read root files from the txt file from 'filelist_700_900.txt'
with open('filelist_700_900.txt') as f:
    filelist = [line.strip() for line in f if line.strip()]

filelist = ['root://cms-xrd-global.cern.ch/' + line if line.startswith('/') else line for line in filelist]

process.source = cms.Source("PoolSource",
    fileNames=cms.untracked.vstring(*filelist)
)

process.TFileService = cms.Service("TFileService",
    fileName=cms.string("lhe_gen_sep_700_900.root")
)

process.LHEMttbarAnalyzer = cms.EDAnalyzer("LHEMttbarAnalyzer",
    lheSrc = cms.InputTag("externalLHEProducer", "", "GEN")
)

process.p = cms.Path(process.LHEMttbarAnalyzer)


