# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21113021.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 21113021
#
# ASCII decay Descriptor: [D+ -> ( eta' -> mu+ mu- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 21113021
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_etaprimepi,mm=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ -> ( eta_prime -> ^mu+ ^mu- ) ^pi+]CC'
tightCut.Cuts      =    {
    '[mu+]cc'  : ' inAcc & dauCuts',
    '[pi+]cc'  : ' inAcc & dauCuts',
    '[D+]cc'   : 'Dcuts' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'dauCuts = ( (GPT > 225 * MeV) & ( GP > 1800 * MeV))',
    'Dcuts = (GPT > 900 * MeV)' ]

