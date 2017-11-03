# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27162412.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 27162412
#
# ASCII decay Descriptor: [D*0 -> (D0 -> K- pi+) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 27162412
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst0_D0pi0,Kpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = '^[D*(2007)0 -> ^(D0 ==> ^K- ^pi+) ^(pi0 ==> ^gamma ^gamma)]CC'
tightCut.Preambulo += [
   'inAcc        = (in_range(0.010, GTHETA, 0.300))',
   'goodD0       = (GP >  4000 * MeV) & (GPT > 400 * MeV)',
   'goodDstar0       = (GP >  4000 * MeV) & (GPT > 400 * MeV)',
   'goodPi0      =   (GP >  400 * MeV) &  (GPT >  200 * MeV)',
   'goodD0Pi  = (GNINTREE( ("pi+"==GABSID) & (GP > 1000 * MeV) & (GPT > 300 * MeV) & inAcc, 1) > 0.5)',
   'goodD0K  = (GNINTREE( ("K-"==GABSID) & (GP > 1000 * MeV) & (GPT > 300 * MeV) & inAcc, 1) > 0.5)',
   'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & ( GPT > 200*MeV ) & (  (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))), 1) > 1.5)'
]
tightCut.Cuts = {
   '[D*(2007)0]cc'          : 'goodDstar0',
   '[D0]cc'          : 'goodD0 & goodD0Pi & goodD0K',
   '[pi0]cc'         : 'goodPi0 & goodPi0Gamma' 
   }

