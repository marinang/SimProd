# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166102.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11166102
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 => (KS0 -> pi+ pi-) pi+ pi-) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (D0 => (KS0 -> pi+ pi-) pi+ pi-) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11166102
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst,KSpipi=DecProdCut,rB=0.3.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
