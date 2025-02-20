import FWCore.ParameterSet.Config as cms

process = cms.Process("PRINT")

# Load MessageLogger and standard services
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# Process a limited number of events (e.g., 10 for testing)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Read input files from a file list
with open('filelist_0_700.txt') as f:
    filelist = [line.strip() for line in f if line.strip()]

# Prepend the global xrootd prefix if needed
filelist = ['root://cms-xrd-global.cern.ch/' + line if line.startswith('/') else line for line in filelist]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*filelist)
)

# Optionally, if you wish to save output (e.g., a TFile with histograms), set up TFileService
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("printLHEWeights_output.root")
)

# Configure the PrintLHEWeights analyzer
process.printLHEWeights = cms.EDAnalyzer("PrintLHEWeights",
    lheSrc = cms.InputTag("externalLHEProducer", "", "GEN")
)

# Define the path to run the analyzer
process.p = cms.Path(process.printLHEWeights)
