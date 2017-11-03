# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/38114002.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 38114002
#
# ASCII decay Descriptor: K_L0 -> mu+ mu- mu+ mu-
#
from Configurables import Generation
Generation().EventType = 38114002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KL_4mu=TighCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 130 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'KL0 => mu+ mu- mu+ mu-'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "decay = in_range ( -1 * meter, GFAEVX ( GVZ, 100 * meter ), 15 * meter ) ",
    'inAcc = in_range ( 0.010 , GTHETA , 0.400 )',
]
tightCut.Cuts      =    {
    'KL0'  : ' decay ',
                        }

