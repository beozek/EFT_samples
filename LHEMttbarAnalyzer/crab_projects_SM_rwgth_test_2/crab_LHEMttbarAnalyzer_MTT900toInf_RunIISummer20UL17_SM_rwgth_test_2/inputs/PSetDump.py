import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/042383E2-DEA9-FE4A-B373-5EBD52D45D94.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/3B8E5807-BD94-2C42-BEEF-80739D50D2AE.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/63583524-0147-5241-AF25-224B2FF3179D.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/A525BF68-D05D-F949-858F-8180D6295438.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/05D30B91-CAFB-5345-A97A-CEA06BADFF8D.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/3BDFCDC6-BAA7-E941-B9C9-F6A504863479.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/66BD19E9-D12F-B846-8BD0-D9FD8F47EF18.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/A5761B73-601E-AF4C-A721-443F8404BC97.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/05F64EF1-ACF9-1649-8D55-DDD105FEBFDE.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2820000/3F5D2F9F-78D1-0C4F-9C05-FDC3873A1B33.root'
    )
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.LHEMttbarAnalyzer = cms.EDAnalyzer("LHEMttbarAnalyzer",
    lheSrc = cms.InputTag("externalLHEProducer","","GEN")
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    saveByLumi = cms.untracked.bool(False),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('lhe_SM_900Inf.root')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.p = cms.Path(process.LHEMttbarAnalyzer)


