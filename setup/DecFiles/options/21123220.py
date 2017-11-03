# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21123220.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 21123220
#
# ASCII decay Descriptor: [D- -> pi- (eta -> e+ e- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 21123220
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pieta,eeg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ -> ^pi+ ( eta -> ^e+ ^e- gamma )]CC'
tightCut.Cuts      =    {
    '[e+]cc'  : ' inAcc & eCuts',
    '[pi+]cc'  : ' inAcc & piCuts',
    '[D+]cc'   : 'Dcuts' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'eCuts = ( (GPT > 100 * MeV) & ( GP > 600 * MeV))',
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]

