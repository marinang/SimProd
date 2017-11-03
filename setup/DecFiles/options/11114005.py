# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114005.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11114005
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114005
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstmumu,phsp=DecProdCut,MomCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
