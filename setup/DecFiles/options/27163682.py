# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163682.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 27163682
#
# ASCII decay Descriptor: [D_s1(2460)+ -> ( D_s0*+ -> (D_s+ -> ( (phi(1020) -> K+ K-) ) pi+ ) pi0) gamma ]cc
#
from Configurables import Generation
Generation().EventType = 27163682
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2460_Ds2317gamma,Dspi0,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 20433,-20433 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s1(2460)+ => (D*_s0+ => (D_s+ => ( (phi(1020) => ^K+ ^K-) ) ^pi+ ) (pi0 -> ^gamma ^gamma) ) ^gamma ]CC'
tightCut.Cuts      =    {
    '[K+]cc'         : ' goodKaon ' , 
    '[pi+]cc'        : ' goodPion ' , 
    'gamma'          : ' goodPhoton' } 

tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPhoton = ( GPT > 0.3  * GeV ) & inAcc' ] 


