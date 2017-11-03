# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574080.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11574080
#
# ASCII decay Descriptor: [B0 -> (D- -> (K*0 -> K+ pi-) e- anti-nu_e) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 11574080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,Kstenu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
