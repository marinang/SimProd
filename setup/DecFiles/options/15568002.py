# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15568002.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 15568002
#
# ASCII decay Descriptor: Lambda_b0 -> ( Lambda_c(2595)+ -> (Lambda_c+ -> ^p+  ^K- ^pi+ )  pi+ pi- )  (tau- -> pi- pi- pi+  nu_tau ) nu_tau~
#
from Configurables import Generation
Generation().EventType = 15568002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593taunu,Lcpipi,ppiK,3pi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ Lambda_b0 -> ( Lambda_c(2595)+ -> (Lambda_c+ -> ^p+  ^K- ^pi+ )  pi+ pi- )  (tau- -> pi- pi- pi+  nu_tau ) nu_tau~ ]CC'
tightCut.Cuts      =    {
    '[p+]cc'   : ' goodProton ' ,
    '[K+]cc'   : ' goodKaon ' ,
    '[pi+]cc'  : ' goodPion ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    'goodProton = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ,
    'goodPion = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ,
    'goodKaon = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ]

