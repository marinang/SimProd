# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23101401.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 23101401
#
# ASCII decay Descriptor: [D_s- -> pi- ( pi0 -> gamma gamma )]cc
#
from Configurables import Generation
Generation().EventType = 23101401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pi+pi0,gg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D_s+ -> ^pi+ ( pi0 -> gamma gamma )]CC'
tightCut.Cuts      =    {
    '[pi+]cc'  : ' inAcc & piCuts',
    '[D_s+]cc' : ' Dcuts ' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]

