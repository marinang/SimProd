# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11995200.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11995200
#
# ASCII decay Descriptor: [[B0] ==> (D*- -> (D~0 -> K+ mu- nu_mu~)) (D_s*+ -> gamma (D_s+ -> K+ K- pi+))]cc
#
from Configurables import Generation
Generation().EventType = 11995200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DD,DD=cocktail,D0muTightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[B0 ==> ^((Charm) -> ^mu+ nu_mu ... ) ^(D~0 -> ^K+ ^pi- ) {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
"from GaudiKernel.SystemOfUnits import mrad" ,
"FilterD = GNINTREE (GCHARM, HepMC.parents)",
"FromD   = 1 == FilterD",
"BCut = (GTHETA < 400.0*mrad)"

]
tightCut.Cuts    =    {
'[mu+]cc'     : "FromD",
'[B0]cc'      : "BCut"
}


