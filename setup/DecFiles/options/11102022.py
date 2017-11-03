# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102022.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11102022
#
# ASCII decay Descriptor: [B0 -> K+ K-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Hb2hh.py" )
from Configurables import Generation
Generation().EventType = 11102022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-=tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
