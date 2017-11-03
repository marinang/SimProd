# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164414.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11164414
#
# ASCII decay Descriptor: {[[B0]nos -> pi+ (D*(2010)- -> pi0 (D- -> K+ K- pi-))]cc, [[B0]os -> pi- (D*(2010)+ -> pi+ (D+ -> K- K+ pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11164414
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-pi+,D-pi0,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
