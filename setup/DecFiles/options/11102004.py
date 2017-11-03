# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102004.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11102004
#
# ASCII decay Descriptor: {[[B0]nos -> K+ pi-]cc, [[B0]os -> K- pi+]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Hb2hh.py" )
from Configurables import Generation
Generation().EventType = 11102004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+pi-=CPV,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
