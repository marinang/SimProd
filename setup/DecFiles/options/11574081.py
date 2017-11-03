# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574081.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11574081
#
# ASCII decay Descriptor: [B0 -> (D- -> (K*0 -> K+ pi-) mu- anti-nu_mu) e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 11574081
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Denu,Kstmunu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
