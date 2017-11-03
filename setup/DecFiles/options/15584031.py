# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15584031.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15584031
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- e+ nu_e) e- anti-nu_e p+]cc
#
from Configurables import Generation
Generation().EventType = 15584031
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0penu,D0=Kenu,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 => (D0 -> ^K- ^e+ nu_e) ^e- nu_e~ ^p+ ]CC"
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[e-]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[e+]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)"
  }

