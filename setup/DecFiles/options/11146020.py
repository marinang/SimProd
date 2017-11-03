# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11146020.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11146020
#
# ASCII decay Descriptor: [B0 -> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) (rho0 ->pi+ pi-)) K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11146020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_X3872Kpi,Jpsirho,mm=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
