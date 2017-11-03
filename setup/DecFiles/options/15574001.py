# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574001.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 15574001
#
# ASCII decay Descriptor: Lambda_b0 -> (Lambda_c+ -> ^p+  ^K- ^pi+ ) ^mu- nu_mu~
#
from Configurables import Generation
Generation().EventType = 15574001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,ppiK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ Lambda_b0 ->  (Lambda_c+ -> ^p+  ^K- ^pi+ )  ^mu-  nu_mu~ ]CC'
tightCut.Cuts      =    {
    '[mu-]cc'  : ' goodMuon ' ,
    '[p+]cc'   : ' goodProton ' ,
    '[K+]cc'   : ' goodKaon ' ,
    '[pi+]cc'  : ' goodPion ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    'goodMuon = ( GPT > 0.6 * GeV ) & ( GP > 2.8 * GeV ) & inAcc ' ,
    'goodProton = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ,
    'goodPion = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ,
    'goodKaon = ( GPT > 0.2 * GeV ) & ( GP > 1.8 * GeV ) & inAcc ' ]

