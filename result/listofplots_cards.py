try:
    ## the normal way to import from rootplot
    from rootplot.tree2hists import RootTree, Plot
except ImportError:
    ## special import for CMSSW installations of rootplot
    from PhysicsTools.PythonAnalysis.rootplot.tree2hists import RootTree, Plot
from array import array      # to allow making Float_t arrays for ROOT hists
from math import pi
from ROOT import TH1D, TH2F  # import other kinds of hists as neeeded

#bdtplot =  Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
#bdtplot =  Plot("BDT"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1.0, 0.5))
#bdtplot =  Plot("bdt_paper"           , TH1D("bdt"    , ";BDT;entries/bin", 17, -0.6, 1.))
#bdtplot =  Plot("BDTninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 32, -0.6, 1.))
#bdtplot =  Plot("Gradninejet.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 10, -5., 5.))
#bdtplot =  Plot("BDTjetsplit.BDTjetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
#bdtplot =  Plot("BDTjetsplit.MVAoutput"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
#bdtplot =  Plot("BDTjetsplit.BDTjetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))
#bdtplot =  Plot("BDT9and10jetsplit.BDT9and10jetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 30, -1., 0.5))
#bdtplot =  Plot("BDT9and10jetsplit.BDT9and10jetsplit"           , TH1D("bdt"    , ";BDT;entries/bin", 50, -1., 1.))

#	Plot("multitopness"   , TH1D("bdt"     , "; Topness;entries/bin", 105, -0.7, 0.35))
#	Plot("HTb"            , TH1D("bdt"     , ";HTB (GeV);entries/bin", 25, 0., 1000.))
#	Plot("HTH"            , TH1D("bdt"     , ";HTH;entries/bin", 100, 0.1, 1.1))
#bdtplot =	Plot("LeptonPt"       , TH1D("bdt"    , ";Lepton p_{T} (GeV);entries/bin", 20, 0., 800.))
#	Plot("SumJetMassX"    , TH1D("bdt"     , ";Sum jet M (GeV);entries/bin", 50, 0., 3500.))
bins_njetsw = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0])
bdtplot = 	Plot("NjetsW"         , TH1D("bdt"    , ";p_{T} weighted jet multiplicity;entries/bin", 20, -0.5, 15.5))
#	Plot("HTX"            , TH1D("bdt"     , ";HTX;entries/bin", 20, 0., 3000.))
#	Plot("csvJetcsv3"     , TH1D("bdt"     , ";CSV3;entries/bin", 100, 0., 1.))
#	Plot("csvJetcsv4"     , TH1D("bdt"     , ";CSV4;entries/bin", 100, 0., 1.))
#	Plot("1stjetpt"       , TH1D("bdt"    , ";1st jet p_{T} (GeV);entries/bin", 50, 0., 1500.))
#	Plot("2ndjetpt"       , TH1D("bdt"    , ";2nd jet p_{T} (GeV);entries/bin", 50, 0., 1000.))
#	Plot("5thjetpt"       , TH1D("bdt"    , ";5th jet p_{T} (GeV);entries/bin", 20, 30., 250.))
#	Plot("6thjetpt"       , TH1D("bdt"    , ";6th jet p_{T} (GeV);entries/bin", 20, 30., 200.))
#	Plot("csvJetpt3"      , TH1D("bdt"     , ";CSV3;entries/bin", 100, 0., 1.))
#	Plot("csvJetpt4"      , TH1D("bdt"     , ";CSV4;entries/bin", 100, 0., 1.))
lp_cards = [bdtplot]


#Example non-uniform binning
#bins_et     = array("f", [15.0, 20.0, 30.0, 50.0, 80.0, 120.0]) # example custom bins
#Plot("et"           , TH1F("pho_et_binned"    , "Lead #gamma: E_{T};E_{T} (GeV);entries/bin", len(bins_et)-1, bins_et)),

