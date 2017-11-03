# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11502020.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11502020
#
# ASCII decay Descriptor: {[[B0]nos -> (tau+ -> pi+ pi- pi+ anti-nu_tau) (tau- -> pi+ pi- pi- nu_tau) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (tau- -> pi+ pi- pi- nu_tau)(tau+ -> pi+ pi- pi+ anti-nu_tau) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11502020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttautau,3pi3pi=DecProdCut,TightCut2,tauolababar.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ ^(B0 ==>  ^(K*(892)0 -> ^K+ ^pi-) ^(tau+ ==> ^pi+ ^pi- ^pi+ nu_tau~) ^(tau- ==> ^pi- ^pi+ ^pi- nu_tau) ) ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  
]
tightCut.Cuts = {
'[B0]cc'       : " ( GPT > 8 * GeV ) & ( GP > 60 * GeV ) " ,
'[K*(892)0]cc' : " ( GPT > 1 * GeV ) & ( GP > 10 * GeV ) " ,
'[tau+]cc'     : " ( GPT > 2 * GeV ) & ( GP > 20 * GeV ) " ,
'[K+]cc'       : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 250 * MeV ) & ( GP > 4 * GeV ) " ,
'[pi-]cc'      : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 250 * MeV ) & ( GP > 2 * GeV ) "
}

