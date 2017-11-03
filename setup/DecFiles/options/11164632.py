# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164632.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11164632
#
# ASCII decay Descriptor: {[[B0]nos -> (D_1- -> (D*(2007)~0 -> {(D~0 -> K+ pi-) (pi0 -> gamma gamma), (D~0 -> K+ pi-) gamma} ) pi- ) pi+ ]cc, [[B0]os -> (D_1- -> (D*(2007)0 -> {(D0 -> K- pi+) (pi0 -> gamma gamma), (D0 -> K- pi+) gamma} ) pi+ ) pi- ]cc}
#
from Configurables import Generation
Generation().EventType = 11164632
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D1pi,Dst0pi,D0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
