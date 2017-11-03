# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11876131.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11876131
#
# ASCII decay Descriptor: [B0 -> (D*- -> (anti-D0 -> (K_S0 -> pi+ pi-) K+ K-) pi-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 11876131
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,KSKK=cocktail,hqet,TightCut,LooserCuts,BRcorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[Beauty --> ^(D*(2010)- => ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^pi-) ^mu+ ... ]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GP > 35000 * MeV) & (GPT > 1500 * MeV) & (GFAEVX(abs(GVZ), 0) - GFAPVX(abs(GVZ), 0) > 1.6 * millimeter)',
    'goodDst      = (GP > 15000 * MeV) & (GPT > 750 * MeV)',
    'goodD        = (GP > 13000 * MeV) & (GPT > 500 * MeV)',
    'goodKS       = (GP > 4000 * MeV) ',
    'goodDDaugK   = (GNINTREE (("K+"  == GABSID) & (GP > 750 * MeV) & inAcc, 4) > 1.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 1750 * MeV) & inAcc, 4) > 1.5)',
    'goodDstDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 1000 * MeV) & inAcc, 1) > 0.5)',
    'goodMuon     = (GNINTREE (("mu+" == GABSID) & (GP > 4000 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts      =    {
    '[B0]cc'         : 'goodB  & goodMuon',
    '[D*(2010)-]cc'  : 'goodDst & goodDstDaugPi',
    '[D0]cc'         : 'goodD  & goodDDaugK',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi'
    }

