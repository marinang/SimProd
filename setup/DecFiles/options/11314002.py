# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11314002.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11314002
#
# ASCII decay Descriptor: {[B0 -> (rho0 -> pi+ pi-) e+ mu-]cc, [B0 -> (rho0 -> pi- pi+) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 11314002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhoemu,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
