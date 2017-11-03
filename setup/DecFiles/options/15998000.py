# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15998000.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 15998000
#
# ASCII decay Descriptor: [[Lambda_b0] ==> (Lambda_c(2595)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-) (D_s*- -> (D_s- -> K+ K- pi-))]cc
#
from Configurables import Generation
Generation().EventType = 15998000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcD,LcD=cocktail,LcmuTightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = "[Lambda_b0 ==> ^((Charm) -> ^mu- nu_mu~ ... ) ^(Lambda_c+ -> ^p+ ^K- ^pi+) {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
"from GaudiKernel.SystemOfUnits import mrad" ,
"FilterD = GNINTREE (GCHARM, HepMC.parents)",
"FromD   = 1 == FilterD",
"BCut = (GTHETA < 400.0*mrad)"

]
tightCut.Cuts    =    {
'[mu-]cc'       : "FromD",
'[Lambda_b0]cc' : "BCut"
}


