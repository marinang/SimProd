# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21123230.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 21123230
#
# ASCII decay Descriptor: [D- -> K- (pi0 -> e+ e- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 21123230
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K+pi0,eeg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ -> ^K+ ( pi0 -> ^e+ ^e- gamma )]CC'
tightCut.Cuts      =    {
    '[e+]cc'  : ' inAcc & eCuts',
    '[K+]cc'  : ' inAcc & piCuts',
    '[D+]cc'  : ' Dcuts ' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'eCuts = ( (GPT > 50 * MeV) & ( GP > 600 * MeV))',
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]

