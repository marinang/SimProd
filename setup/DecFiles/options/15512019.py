# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15512019.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 15512019
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15512019
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pmunu=TightCut,LCSR,M4.5GeV,RH.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 500 )
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut  = Generation().SignalRepeatedHadronization.TightCut

tightCut.Decay = "^[ Lambda_b0 => ^p+ ^mu- nu_mu~  ]CC"

tightCut.Preambulo += [
"from LoKiCore.functions import in_range",
"from GaudiKernel.SystemOfUnits import GeV, MeV" ,
"ACC  = in_range ( 0.0075, GTHETA, 0.400 )"
 ]

tightCut.Cuts = {
   '[Lambda_b0]cc': "GMASS('p+'==GABSID,'mu+'==GABSID) > 4.5*GeV",
   '[p+]cc'       : "ACC & (GPT > 700.*MeV) & (GP > 2500*MeV)",
   '[mu-]cc'      : "ACC & (GPT > 700.*MeV) & (GP > 2500*MeV)"
  }

