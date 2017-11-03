# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164121.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11164121
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 -> pi+ pi-) KS0]cc, [[B0]os -> (D0 -> pi- pi+) KS0]cc}
#
from Configurables import Generation
Generation().EventType = 11164121
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Ks,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
