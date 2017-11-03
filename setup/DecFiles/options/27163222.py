# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163222.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 27163222
#
# ASCII decay Descriptor: [D*_s+ -> (D_s+ -> K+ K- pi+) gamma ]cc
#
from Configurables import Generation
Generation().EventType = 27163222
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dsst_Dsgamma,KKpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 433,-433 ]

from Configurables import LoKi__GenCutTool
gen=Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = Generation().SignalPlain.TightCut
tightCut.Decay     = '[D*_s+ -> (D_s+ -> ^K+ ^K- ^pi+) ^gamma]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import MeV" ,
    "from LoKiCore.functions import in_range"
]
tightCut.Cuts      =    {
    'gamma'   : "( GPT > 300*MeV ) & ( in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ) ) ",
    '[K+]cc'  : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 150 * MeV ) & ( GP > 1600*MeV ) " ,
    '[pi+]cc' : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 150 * MeV ) & ( GP > 1600*MeV ) "
}

