# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144008.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11144008
#
# ASCII decay Descriptor: {[[B0]nos -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho0 -> pi+ pi-)]cc, [[B0]os -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11144008
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsirho0,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
