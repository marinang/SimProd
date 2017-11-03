# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164451.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11164451
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi- pi0) K+]cc, [[B0]os -> (D+ => K- pi+ pi+ pi0) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11164451
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DK,Kpipipi0=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
