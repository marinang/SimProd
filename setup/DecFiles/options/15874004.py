# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15874004.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15874004
#
# ASCII decay Descriptor: [ Lambda_b0 ==>  (Lambda_c+ ==> p+ K- pi+)  mu- anti_nu_mu   ]cc
#
from Configurables import Generation
Generation().EventType = 15874004
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lctaunu,pKpi=cocktail,RLcCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 ==>  ^(Lambda_c+ ==> ^p+ ^K- ^pi+)  (tau- -> ^mu- nu_mu~ nu_tau) nu_tau~ ]CC"
tightCut.Preambulo += [
"from LoKiCore.functions import in_range"  ,
"from GaudiKernel.SystemOfUnits import GeV, MeV",
"pipiKP     = GCHILD(GP,1) + GCHILD(GP,2) + GCHILD(GP,3)" ,
"pipiKPT     = GCHILD(GPT,1) + GCHILD(GPT,2) + GCHILD(GPT,3)" 
 ]
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[K+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500 * MeV) ",
'[Lambda_c+]cc' : "(pipiKP > 15000 *MeV) & (pipiKPT > 2300 *MeV)"
  }

