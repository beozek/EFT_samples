from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'LHEMttbarAnalyzer_MTT0to700_RunIISummer20UL17_sumweights'  # Unique name for this CRAB job
config.General.workArea = 'crab_projects_sumweights'  # Directory where CRAB will store job logs and reports
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg.py'  # CMSSW configuration file
config.JobType.allowUndistributedCMSSW = True 

config.Data.inputDataset = '/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'  # Split jobs by number of files
config.Data.unitsPerJob = 5  # Number of files per job
# config.Data.totalUnits = 50

# Output directory
config.Data.outLFNDirBase = '/store/user/beozek/LHEMttbarAnalyzer/MTT0to700_sumweights/'
config.Data.publication = False
config.Data.outputDatasetTag = 'LHEMttbarAnalyzer_MTT0to700_RunIISummer20UL17_sumweights'

# Site section
config.Site.storageSite = 'T2_DE_DESY'