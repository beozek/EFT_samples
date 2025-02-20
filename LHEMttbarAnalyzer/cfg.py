import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# Only print progress message every 2000 events
process.MessageLogger.cerr.FwkReport.reportEvery = 2000

# Process all events (-1 means no limit)
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))

# Read file from 'filelist_700_900.txt'
with open('filelist_0_700.txt') as f:
    filelist = [line.strip() for line in f if line.strip()]

filelist = ['root://cms-xrd-global.cern.ch/' + line if line.startswith('/') else line for line in filelist]

process.source = cms.Source("PoolSource",
    fileNames=cms.untracked.vstring(*filelist)
)

process.TFileService = cms.Service("TFileService",
    fileName=cms.string("lhe_SM_0_700.root")
)

process.LHEMttbarAnalyzer = cms.EDAnalyzer("LHEMttbarAnalyzer",
    lheSrc = cms.InputTag("externalLHEProducer", "", "GEN")
)

process.p = cms.Path(process.LHEMttbarAnalyzer)


