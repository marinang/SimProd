# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166510.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11166510
#
# ASCII decay Descriptor: [B0 -> (rho0 -> pi+ pi-) (anti-D*0 -> (anti-D0 -> (K_S0 -> pi+ pi-) K+ K-) (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 11166510
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0rho0,D0pi0,KSKK=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B0 => ^(D*(2007)~0 -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^(pi0 -> ^gamma ^gamma)) ^(rho(770)0 => ^pi+ ^pi-)]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.400))',
   'goodB       = (GP > 35000 * MeV) & (GPT > 3500 * MeV) & (GTIME > 0.060 * millimeter)',
   'goodDstar0       = (GP >  25000 * MeV) & (GPT > 4250 * MeV)',
   'goodD0       = (GP >  22500 * MeV) & (GPT > 3750 * MeV)',
   'goodD0K  = (GNINTREE( ("K+"==GABSID) & (GP > 1000 * MeV) & (GPT > 100 * MeV) & inAcc, 1) > 1.5)',
   'goodKSPi  = (GNINTREE( ("pi+"==GABSID) & (GPT >  50 * MeV) & (GP >  1900 * MeV) & inAcc, 1) > 1.5)',
   'goodKS       = (GP >  3500 * MeV) & (GPT > 400 * MeV) ',
   'goodRho0Pi = (GNINTREE( ("pi+"==GABSID) & (GP > 4500 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & ( (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))) , 1) > 0.5)'
]
tightCut.Cuts = {
   '[B0]cc'          : 'goodB',
   '[D*(2007)0]cc'   : 'goodDstar0',
   '[rho(770)0]cc'   : 'goodRho0Pi',
   '[pi0]cc'         : 'goodPi0Gamma',
   '[D0]cc'          : 'goodD0 & goodD0K',
   '[KS0]cc'         : 'goodKS & goodKSPi',
   }

