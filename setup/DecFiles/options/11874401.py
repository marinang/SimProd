# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874401.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11874401
#
# ASCII decay Descriptor: [[B0] ==> mu+ nu_mu (D*- -> (D- -> K+ pi- pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11874401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D+Xmunu,D+=cocktail.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
