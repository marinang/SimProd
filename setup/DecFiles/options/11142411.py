# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11142411.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11142411
#
# ASCII decay Descriptor: [ B0 -> (J/psi(1S) -> mu+ mu-) (K_S0 -> pi0 pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 11142411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKS,mmpi0pi0=OnePi0ReqInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/OnePi0ReqInAcc"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'OnePi0ReqInAcc')
pi0mmInAcc = Generation().SignalRepeatedHadronization.OnePi0ReqInAcc
pi0mmInAcc.Decay = '[B0 -> (J/psi(1S) -> ^mu+ ^mu-) ^(KS0 -> ^pi0 ^pi0)]CC'
pi0mmInAcc.Preambulo += [
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'KSDaugPiInAcc = (GNINTREE( ("pi0"==GABSID) & inAcc) >= 1)',
]
pi0mmInAcc.Cuts = {
   '[KS0]cc'  : 'KSDaugPiInAcc',
   'mu+'      : 'inAcc',
   'mu-'      : 'inAcc'
   }

