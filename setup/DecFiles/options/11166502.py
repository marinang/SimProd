# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166502.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11166502
#
# ASCII decay Descriptor: [B0 ->  (D*(2010)- -> (anti-D0 -> ((K_S0 -> pi+ pi-) pi+ pi- (pi0 -> gamma gamma)))  pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166502
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstPi,D0pi,Kspipipi0=TightCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B0 -> ^(D*(2010)- -> ^(D~0 => ^(KS0 ==> ^pi+ ^pi-) ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma)) pi-) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
    'goodB        = (GP > 7500 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.105 * millimeter)',
    'goodD        = (GP > 4000 * MeV) & (GPT > 400 * MeV)',
    'goodKS       = (GNINTREE(("KS0"==GABSID) & (GP >  4000 * MeV) & (GPT >  400 * MeV) & (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter))>0.5)',
    'goodDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 750 * MeV) & inAcc, 1) > 1.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 500 * MeV) & inAcc, 1) > 1.5)',
    'goodBachPi   = (GNINTREE (("pi+" == GABSID) & (GP > 5000 * MeV) & (GPT > 500 * MeV) & inAcc, 1) > 0.5)',
    'goodPi0      =  (GNINTREE( ("pi0"==GABSID) & (GP > 750 * MeV) & (GPT > 300 * MeV) & inAcc, 1) > 0.5)',
    'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & (GP > 750 * MeV) & (GPT > 400 * MeV) & inEcalX  & inEcalY  & inAcc, 1) > 1.5)',
]
tightCut.Cuts      =    {
    '[B0]cc'         : 'goodB  & goodBachPi',
    '[D0]cc'         : 'goodD & goodDaugPi & goodPi0 & goodKS' ,
    '[KS0]cc'        : 'goodKsDaugPi',
    '[pi0]cc'        : 'goodPi0Gamma',
    }

