# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11442001.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11442001
#
# ASCII decay Descriptor: {[B0 => (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) X]cc, [B0 => (psi(2S) -> mu+ mu- {,gamma} {,gamma} X]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CharmoniumInAcc.py" )
from Configurables import Generation
Generation().EventType = 11442001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiX,mm=JpsiInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "SelectedDaughterInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
