# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164010.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11164010
#
# ASCII decay Descriptor: {[[B0]nos -> (D0 -> K- pi+) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (D~0 -> K+ pi-) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst,Kpi=OS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
