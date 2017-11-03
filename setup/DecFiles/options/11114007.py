# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114007.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11114007
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114007
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenInPhSpDecay
ToolSvc().addTool( EvtGenInPhSpDecay )
ToolSvc().EvtGenInPhSpDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstmumu,phsp=DecProdCut,MomCut,WeightMax.dec"
Generation().DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.DecayTool = "EvtGenInPhSpDecay"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
ToolSvc().EvtGenInPhSpDecay.MaxQ2Bins = 20
ToolSvc().EvtGenInPhSpDecay.MaxEvtGenCalls = 1500
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
