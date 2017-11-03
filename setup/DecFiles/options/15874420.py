# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15874420.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15874420
#
# ASCII decay Descriptor: [ Lambda_b0 ==>  (Lambda_c+ ==> p+ K- pi+) pi0 pi0  mu- anti_nu_mu  ]cc
#
from Configurables import Generation
Generation().EventType = 15874420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcpi0pi0munu,pX=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 ==>  (Lambda_c+ ==> ^p+ {X} {X} {X} {X}) pi0 pi0 ^mu- nu_mu~ {X} {X} {X} {X}  ]CC"
tightCut.Preambulo += [
"from LoKiCore.functions import in_range"  ,
"from GaudiKernel.SystemOfUnits import GeV, MeV",
"pmuPX = GCHILD(GPX,('p+' == GABSID )) + GCHILD(GPX,('mu-' == GABSID))",
"pmuPY = GCHILD(GPY,('p+' == GABSID )) + GCHILD(GPY,('mu-' == GABSID))",
"pmuPT2 = pmuPX * pmuPX + pmuPY * pmuPY"
 ]
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 950 * MeV ) & (GP > 14600 * MeV)" ,
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GPT > 1450 * MeV) &  (GP > 4900 * MeV) ",
'[Lambda_b0]cc' : "pmuPT2 > 1960000"
  }

