# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31113009.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 31113009
#
# ASCII decay Descriptor: [tau+ -> anti-p- mu+ mu+]cc
#
from Configurables import Generation
Generation().EventType = 31113009
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau+_anti-p-mu+mu+=FromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ ^(tau+ -> ^p~- ^mu+ ^mu+) ]CC'
tightCut.Cuts      =    {
    '[mu+]cc'  : ' goodMuon ' , 
    '[p~-]cc'  : ' goodProton ' , 
    '[tau+]cc' : ' goodTau  ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodProton = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodTau  = ~GHAS (GCHARM, HepMC.ancestors) ' ]


