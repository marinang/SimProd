# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15102512.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 15102512
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (eta -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15102512
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_etaLambda,gg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[Lambda_b0 -> ^(eta -> ^gamma ^gamma) ^(Lambda0 -> ^p+ ^pi-)]CC'
tightCut.Cuts      =    {
    '[Lambda_b0]cc': ' goodLb    ' ,
    '[Lambda0]cc'  : ' goodL     ' ,
    '[pi+]cc'      : ' goodPion  ' ,
    '[p+]cc'       : ' goodProton' ,
    '[eta]cc'      : ' goodEta   ' ,
    'gamma'        : ' goodGamma ' }
tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodLb     = ( GPT > 1000 * MeV ) ' , 
    'goodL      = ( GPT > 1000 * MeV ) ' ,
    'goodEta    = ( GPT > 2000 * MeV ) ' ,
    'goodPion   = ( GPT > 300 * MeV ) & inAcc ' , 
    'goodProton = ( GPT > 300 * MeV ) & inAcc ' , 
    'goodGamma  = ( GPT > 500 * MeV ) & inAcc ' ]


