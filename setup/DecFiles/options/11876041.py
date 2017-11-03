# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11876041.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11876041
#
# ASCII decay Descriptor: [B0 -> (D*- -> (anti-D0 -> K+ pi- pi- pi+) pi-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 11876041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,Kpipipi=cocktail,hqet,AMPGEN,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ B~0 ==> ^( D*(2010)+ -> ^( D0 -> ^K- ^pi+ ^pi+ ^pi- ) ^pi+ {gamma} {gamma} {gamma} {gamma} ) ^mu- nu_mu~ {X} {X} {X} {X} {X} ]CC"

tightCut.Preambulo += [
  "from LoKiCore.functions import in_range"  ,
  "from GaudiKernel.SystemOfUnits import GeV, MeV",
  "inAcc = in_range(0.005,GTHETA,0.4)"
 ]

tightCut.Cuts = {
  '[mu+]cc'       : "inAcc & (GPT > 1.00 * GeV) & (GP > 3.0 * GeV )",
  '[pi+]cc'       : "inAcc & (GPT > 0.10 * GeV) ",
  '[K+]cc'        : "inAcc & (GPT > 0.25 * GeV) & (GP > 1.8 * GeV )",
  '[D0]cc'        : "(GPT > 1.6 * GeV) & (GCHILD(GPT,2) > 0.25 * GeV) & (GCHILD(GP,2) > 1.8 * GeV ) & (GCHILD(GPT,3) > 0.25 * GeV) & (GCHILD(GP,3) > 1.8 * GeV ) & (GCHILD(GPT,4) > 0.25 * GeV) & (GCHILD(GP,4) > 1.8 * GeV )",
}

