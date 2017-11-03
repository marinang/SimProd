# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31113012.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 31113012
#
# ASCII decay Descriptor: [tau- -> mu- mu- e+]cc
#
from Configurables import Generation
Generation().EventType = 31113012
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mumue=SS,FromB,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ ^(tau- -> ^mu- ^mu- ^e+) ]CC'
tightCut.Cuts      =    {
    '[e+]cc'  : ' goodElectron ' ,
    '[mu+]cc'  : ' goodMuon ' , 
    '[tau+]cc' : ' goodTau  ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodElectron = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' ,
    'goodMuon = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' , 
    'goodTau  = ~GHAS (GCHARM, HepMC.ancestors) ' ]


