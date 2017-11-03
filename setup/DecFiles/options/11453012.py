# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11453012.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11453012
#
# ASCII decay Descriptor: { [B0 => (psi(2S) -> e+ e-) X]cc }
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CharmoniumInAcc.py" )
from Configurables import Generation
Generation().EventType = 11453012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SX,ee=JpsiInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "SelectedDaughterInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
