# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163491.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 27163491
#
# ASCII decay Descriptor: [D_s0*+ -> (D_s+ -> ( (phi(1020) -> K+ K-) ) pi+ ) (pi0 -> gamma gamma) ]cc
#
from Configurables import Generation
Generation().EventType = 27163491
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2317_Dspi0,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 10431,-10431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D*_s0+ => (D_s+ => ( (phi(1020) => ^K+ ^K-) ) ^pi+ ) (pi0 -> ^gamma ^gamma) ]CC'
tightCut.Cuts      =    {
    '[K+]cc'         : ' goodKaon ' , 
    '[pi+]cc'        : ' goodPion ' , 
    'gamma'          : ' goodPhoton' } 

tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPhoton = ( GPT > 0.3  * GeV ) & inAcc' ] 


