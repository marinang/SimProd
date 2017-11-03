# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574133.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15574133
#
# ASCII decay Descriptor: {[ Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) pi+)  anti-nu_mu mu-]cc}
#
from Configurables import Generation
Generation().EventType = 15574133
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,Relaxed_L0Pi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut  = Generation().SignalPlain.TightCut
tightCut.Decay = "[ Lambda_b0 ==>  ^(Lambda_c+ ==> ^(Lambda0 ==>^p+ ^pi-) ^pi+ {X} {X} {X} {X} {X} )  ^mu- nu_mu~ {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
"from LoKiCore.functions import in_range"  ,
"from GaudiKernel.SystemOfUnits import GeV, MeV",
 ]
tightCut.Cuts      =    {
'[mu-]cc'  : "  (GP > 700 * MeV) & (GPT > 350 * MeV)  "
  }

