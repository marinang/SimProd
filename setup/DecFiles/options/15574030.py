# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574030.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 15574030
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- pi+) mu- anti-nu_mu p+]cc
#
from Configurables import Generation
Generation().EventType = 15574030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0pmunu,D0=Kpi,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 => (D0 -> ^K- ^pi+) ^mu- nu_mu~ ^p+ ]CC"
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[pi+]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 800 * MeV ) & (GP > 3000 * MeV)"
  }

