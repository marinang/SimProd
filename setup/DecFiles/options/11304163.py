# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11304163.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11304163
#
# ASCII decay Descriptor: {[B0 -> K+ pi- (KS0 -> pi+ pi-)]cc, [B0 -> K- pi+ (KS0 -> pi+ pi-)]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2KShh.py" )
from Configurables import Generation
Generation().EventType = 11304163
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KpiKs=sqDalitz,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
