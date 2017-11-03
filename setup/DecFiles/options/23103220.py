# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23103220.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 23103220
#
# ASCII decay Descriptor: [D_s+ -> ( eta' -> ( rho0 -> pi+ pi- ) gamma) K+]cc
#
from Configurables import Generation
Generation().EventType = 23103220
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_etaprimeK,rhogamma=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
                                                        
                                                                         
from Configurables import LoKi__GenCutTool                               
gen = Generation()                                                       
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )                
tightCut = gen.SignalPlain.TightCut                         
tightCut.Decay     = '^[ D_s+ -> ( eta_prime -> ( rho(770)0 -> ^pi+ ^pi- ) ^gamma ) ^K+]CC'    
tightCut.Cuts      =    {                                   
    '[pi+]cc'    : ' inAcc & dauCuts',                      
    '[K+]cc'    : ' inAcc & dauCuts',                      
    '[D_s+]cc'   : 'Dcuts' }                                
tightCut.Preambulo += [                                     
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' ,          
    'dauCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',   
    'Dcuts = (GPT > 1000 * MeV)' ]  

