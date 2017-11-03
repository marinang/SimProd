# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574090.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15574090
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (D0 -> K- pi+) p+) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15574090
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2840munu,WideLc2840,Lc2840_D0p,D0_Kpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+  62  4122  1.0  2.840 2.0e-024   Lambda_c+  4122  0", "Lambda_c~-  63 -4122 -1.0  2.840 2.0e-024  anti-Lambda_c-  -4122   0.","Lambda_c(2625)+ 104124 104124 1.0 4.880 5.00e-024 Lambda_c(2625)+ 0 1.0e-004", "Lambda_c(2625)~- -104124 -104124 -1.0 4.880 5.00e-024 anti-Lambda_c(2625)- 0 1.0e-004" ]


from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 => (Lambda_c+ -> (D0 -> ^K- ^pi+) ^p+) ^mu- nu_mu~]CC"
tightCut.Cuts      =    {
'[p+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[pi+]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 250 * MeV ) & (GP > 3000 * MeV)",
'[mu-]cc'  : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 800 * MeV ) & (GP > 3000 * MeV)"
}

