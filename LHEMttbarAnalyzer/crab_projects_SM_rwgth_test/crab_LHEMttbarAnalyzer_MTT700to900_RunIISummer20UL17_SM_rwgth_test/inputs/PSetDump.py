import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/1624C360-8C21-3D44-B384-8971CF2D2E0D.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/1AC13883-E179-304E-ADA4-7070CF0C3A6D.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/4E5D1BE3-0659-644F-A9B2-6152A39BDD8C.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/BE593754-C1AC-324E-9ADC-07C2BE3B8288.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/F92947A2-97F8-5040-A991-14993E522776.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/24A0F482-C122-3B4A-92E9-B0F4979B271E.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/86495809-96A1-D945-A2CC-DFE64F6C17D1.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/C7CD380D-64F0-184D-87D6-9F683F99CDEC.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/273D516E-6990-0640-917C-78326C7E9170.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-700to900_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/120000/D6CE8978-FF7B-F344-B2D5-93CEDF8AF607.root'
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
    fileName = cms.string('lhe_SM_700_900.root')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.p = cms.Path(process.LHEMttbarAnalyzer)


