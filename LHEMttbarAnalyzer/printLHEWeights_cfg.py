import FWCore.ParameterSet.Config as cms

process = cms.Process("PRINT")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

with open('filelist_0_700.txt') as f:
    filelist = [line.strip() for line in f if line.strip()]

filelist = ['root://cms-xrd-global.cern.ch/' + line if line.startswith('/') else line for line in filelist]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*filelist)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("printLHEWeights_output.root")
)

\process.printLHEWeights = cms.EDAnalyzer("PrintLHEWeights",
    lheSrc = cms.InputTag("externalLHEProducer", "", "GEN")
)

\process.p = cms.Path(process.printLHEWeights)
