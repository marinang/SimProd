# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574030.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11574030
#
# ASCII decay Descriptor: {[[B0]nos -> (D- -> (K*(892)0 -> K+ pi-) mu- anti-nu_mu) mu+ nu_mu ]cc, [[B0]os -> (D+ -> (K*(892)~0 -> K- pi+) mu+ nu_mu) mu- anti-nu_mu ]cc}
#
from Configurables import Generation
Generation().EventType = 11574030
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,Kstmunu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
