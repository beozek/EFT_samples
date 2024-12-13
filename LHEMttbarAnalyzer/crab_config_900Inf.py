# crab_config.py
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'LHEMttbarAnalyzer_MTT900toInf_RunIISummer20UL17_investigatingTopPt'
config.General.workArea = 'crab_projects_investigatingTopPt'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cfg_900Inf.py'  # CMSSW configuration file
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/user/beozek/LHEMttbarAnalyzer/MTT900toInf_investigatingTopPt/'
config.Data.publication = False
config.Data.outputDatasetTag = 'LHEMttbarAnalyzer_MTT900toInf_RunIISummer20UL17_investigatingTopPt'

config.Site.storageSite = 'T2_DE_DESY'