# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11774410.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11774410
#
# ASCII decay Descriptor: [B0 => (D*(*) => ( D- => pi+ pi- pi- pi0) pi0) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 11774410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dststmunu,3pipi0=cocktail,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> (D- ==> ^pi+ ^pi- ^pi- {X} {X} ) ^mu+ nu_mu {X} {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  
]
tightCut.Cuts      =    {
'[pi+]cc'   : " ( GPT > 250 * MeV ) & ( GP > 2000 * MeV )" ,
'[mu+]cc'  : "  (GPT > 250* MeV) "
   }

