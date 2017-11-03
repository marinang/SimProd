# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166320.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11166320
#
# ASCII decay Descriptor: [B0 -> (rho0 -> pi+ pi-) (anti-D*0 -> (anti-D0 -> (K_S0 -> pi+ pi-) pi+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11166320
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0rho0,D0gamma,KSpipi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B0 => ^(D*(2007)~0 -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^pi+ ^pi-) ^gamma ) ^(rho(770)0 => ^pi+ ^pi-)]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.400))',
   'goodB       = (GP > 32500 * MeV) & (GPT > 2000 * MeV) & (GTIME > 0.060 * millimeter)',
   'goodDstar0       = (GP >  20000 * MeV) & (GPT > 2500 * MeV)',
   'goodD0       = (GP >  17500 * MeV) & (GPT > 2000 * MeV)',
   'goodD0Pi  = (GNINTREE( ("pi+"==GABSID) & (GP > 1000 * MeV) & (GPT > 50 * MeV) & inAcc, 1) > 1.5)',
   'goodKSPi  = (GNINTREE( ("pi+"==GABSID) & (GPT >  50 * MeV) & (GP >  1900 * MeV) & inAcc, 1) > 1.5)',
   'goodKS       = (GP >  3500 * MeV) & (GPT > 250 * MeV) ',
   'goodRho0Pi = (GNINTREE( ("pi+"==GABSID) & (GP > 4500 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodGamma = (GNINTREE( ("gamma"==GABSID) & ( (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))) , 1) > 0.5)'
]
tightCut.Cuts = {
   '[B0]cc'          : 'goodB',
   '[D*(2007)0]cc'   : 'goodDstar0 & goodGamma',
   '[rho(770)0]cc'   : 'goodRho0Pi',
   '[D0]cc'          : 'goodD0 & goodD0Pi',
   '[KS0]cc'         : 'goodKS & goodKSPi',
   }

