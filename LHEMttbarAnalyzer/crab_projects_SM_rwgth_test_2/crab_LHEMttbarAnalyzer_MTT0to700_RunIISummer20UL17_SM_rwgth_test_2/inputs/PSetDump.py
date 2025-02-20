import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830000/087C3F4A-F6EC-9A4A-A77E-78F0CE426883.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830002/2CC0FA2C-A10B-E347-9AB8-E245E6D411E7.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830000/5B24D68A-E121-C246-B333-C1DB2170E478.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830000/D5FBB190-769B-F04B-B06D-80812443CAE3.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830001/E106872E-2EE4-4B4A-88F1-1A76010C2E79.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830002/AAF524AF-EB61-E143-BE4F-BEF1CF36BB31.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830001/00FD1084-49E2-A242-BF03-07D16A1FD096.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830000/4EE2597B-7A62-DA45-91FB-AA7D6D2A6BE3.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830001/13F617F4-BFD8-3548-BFB5-AA4A1C9F48CD.root', 
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v3/2830001/9285D0E9-C3B7-A046-92D5-BAB84E316038.root'
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
            reportEvery = cms.untracked.int32(2000)
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
    fileName = cms.string('lhe_SM_0_700.root')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.p = cms.Path(process.LHEMttbarAnalyzer)


