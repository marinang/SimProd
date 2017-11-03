# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11876130.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11876130
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D*(2010)- => (D~0 -> (KS0 -> pi+ pi-) K+ K-) pi-)]cc, [[B0]os => anti_nu_mu mu- (D*(2010)+ => (D0 -> (KS0 -> pi+ pi-) K+ K-) pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11876130
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,KSKK=cocktail,hqet,TightCut,BRcorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[Beauty => ^(D*(2010)- => ^(D~0 -> ^(KS0 -> ^pi+ ^pi-) ^K+ ^K-) ^pi-) ^Nu ^mu+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GFAEVX(abs(GVZ), 0) - GFAPVX(abs(GVZ), 0) > 1.6 * millimeter)',
    'goodD        = (GP > 20000 * MeV) & (GPT > 1900 * MeV)',
    'goodKS       = (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter)',
    'goodDDaugK   = (GNINTREE (("K+"  == GABSID) & (GP > 2100 * MeV) & inAcc, 4) > 1.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 2500 * MeV) & inAcc, 4) > 1.5)',
    'goodMuon     = (GNINTREE (("mu+" == GABSID) & (GP > 8000 * MeV) & (GPT > 1300 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts      =    {
    '[B0]cc'         : 'goodB  & goodMuon',
    '[D0]cc'         : 'goodD  & goodDDaugK',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi',
    '[mu+]cc'        : 'inAcc'
    }

