# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11496001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11496001
#
# ASCII decay Descriptor: { [B0 -> (D(*)+ -> pi+ pi+ pi-)   (D(*)- -> pi+ pi- pi-)]cc,
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAcc.py" )
from Configurables import Generation
Generation().EventType = 11496001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DD,3body=cocktail,TracksInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
