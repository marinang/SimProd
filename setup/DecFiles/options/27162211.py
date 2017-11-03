# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27162211.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 27162211
#
# ASCII decay Descriptor: [D*0 -> (D0 -> K- pi+) gamma]cc
#
from Configurables import Generation
Generation().EventType = 27162211
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst0_D0gamma,Kpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]

from Configurables import LoKi__GenCutTool
gen=Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = Generation().SignalPlain.TightCut
tightCut.Decay     = '^[D*(2007)0 -> ^(D0 -> ^K- ^pi+) ^gamma]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import MeV" ,
    "from LoKiCore.functions import in_range"
]
tightCut.Cuts      =    {
    'gamma'   : "( GPT > 300*MeV ) & (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019)) ",
    '[K+]cc'  : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 300 * MeV ) & ( GP > 1000*MeV ) " ,
    '[pi+]cc' : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 300 * MeV ) & ( GP > 1000*MeV ) ",
   '[D*(2007)0]cc'          : "(GP >  4000 * MeV) & (GPT > 400 * MeV)",
   '[D0]cc'          : "(GP >  4000 * MeV) & (GPT > 400 * MeV)",
}

