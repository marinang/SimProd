# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21163011.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 21163011
#
# ASCII decay Descriptor: [D+ -> pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 21163011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi+pi-pi+=phsp,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ => ^pi+ ^pi- ^pi+]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import millimeter" ,
    "inAcc = in_range ( 0.010, GTHETA, 0.400 ) " , 
    "daughcuts = ( (GPT > 220 * MeV) & ( GP > 2400 * MeV))",
    "Dcuts = ( (GPT > 2300 * MeV) & ( GP > 20000 * MeV))"
]
tightCut.Cuts      =    {
    '[pi+]cc'  : ' inAcc & daughcuts',
    '[D+]cc'   : 'Dcuts'
                        }

