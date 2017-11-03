# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23103012.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 23103012
#
# ASCII decay Descriptor: [D_s+ -> pi- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 23103012
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_pi-pi+pi+=phsp,TightCut2.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D_s+ => ^pi- ^pi+ ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter' ,
    'inAcc = in_range ( 0.010, GTHETA, 0.400 ) ' , 
    'daughcuts = ( (GPT > 250 * MeV) & ( GP > 2000 * MeV))',
    'Dcuts = ( (GPT > 2100 * MeV) & ( GP > 14000 * MeV))'
]
tightCut.Cuts      =    {
    '[pi+]cc'  : ' inAcc & daughcuts',
    '[D_s+]cc'   : 'Dcuts'
                        }

