# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164092.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11164092
#
# ASCII decay Descriptor: {[[B0]nos -> K+ (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os -> K- (D*(2010)+ -> pi+ (D0 -> K- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11164092
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-K+,D0pi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
