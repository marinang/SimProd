# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21103010.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 21103010
#
# ASCII decay Descriptor: [D+ -> K- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21103010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-pi+pi+=res,DecProdCut,pt10GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/MinPTAndDaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'MinPTAndDaughtersInLHCb' )
minPTAndDaughtersInLHCb = gen.SignalPlain.MinPTAndDaughtersInLHCb
minPTAndDaughtersInLHCb.Decay     = '^[D+ => ^K- ^pi+ ^pi+]CC'
minPTAndDaughtersInLHCb.Preambulo += [
    'from GaudiKernel.SystemOfUnits import MeV ',
    'inAcc     = in_range ( 0.010 , GTHETA , 0.400 ) ',
    'DPT       = ( GPT > 10000 * MeV )'
]
minPTAndDaughtersInLHCb.Cuts      =    {
    '[pi+]cc'         : 'inAcc',
    '[K+]cc'          : 'inAcc',
    '[D+]cc'          : 'DPT',
    }


