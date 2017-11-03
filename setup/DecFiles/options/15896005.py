# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15896005.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15896005
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s- -> (tau- -> mu- anti-nu_mu nu_tau) anti-nu_tau) (Lambda_c(2625)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15896005
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2625Ds,Lcpipi,ppiK,semileptonic=RLcstCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 ==>  ^(Lambda_c+ ==> ^p+ ^K- ^pi+ {X} {X} {X} {X})  ^mu- nu_mu~ {X} {X} {X} {X} {X} {X} {X} ]CC"
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

