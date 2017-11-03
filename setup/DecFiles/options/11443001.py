# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11443001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11443001
#
# ASCII decay Descriptor: [[B0]nos => (J/psi(1S) -> e+ mu-) X]CC
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/CharmoniumInAcc.py" )
from Configurables import Generation
Generation().EventType = 11443001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiK1,emurhoK=cocktail,JpsiInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "SelectedDaughterInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
