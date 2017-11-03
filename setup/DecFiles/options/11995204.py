# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11995204.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11995204
#
# ASCII decay Descriptor: [[B0] ==> (D*- -> (D~0 -> K+ mu- nu_mu~)) (D_s*+ -> gamma (D_s+ -> K+ K- pi+))]cc
#
from Configurables import Generation
Generation().EventType = 11995204
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DD,DD=cocktail,D+muRDplusCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[B0 ==> ((Charm) -> ^mu+ nu_mu ... ) ^(D- -> ^K+ ^pi- ^pi-) {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "pipiKP     = GCHILD(GP,1) + GCHILD(GP,2) + GCHILD(GP,3)" ,
 "pipiKPT     = GCHILD(GPT,1) + GCHILD(GPT,2) + GCHILD(GPT,3)" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 150 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500* MeV) ",
'[D+]cc'   : "( pipiKP > 15000 * MeV ) & (pipiKPT > 2300 * MeV)"
   }

