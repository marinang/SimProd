# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102261.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11102261
#
# ASCII decay Descriptor: {[[B0]nos ->  K+ pi- gamma ]cc , [[B0]os -> K- pi+ gamma]cc}
#
from Configurables import Generation
Generation().EventType = 11102261
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kpigamma=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
