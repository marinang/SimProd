# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144050.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11144050
#
# ASCII decay Descriptor: {[[B0]nos -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) K+ pi-]cc, [[B0]os -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 11144050
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKpi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
