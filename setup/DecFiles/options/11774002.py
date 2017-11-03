# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11774002.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11774002
#
# ASCII decay Descriptor: {B~0 => (D_0*+ => (D_s+ => K+ K- pi+) anti-K0) anti-nu_mu mu-]cc}
#
from Configurables import Generation
Generation().EventType = 11774002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstp2400munu,DsKS0,KKpi=LHCbAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
