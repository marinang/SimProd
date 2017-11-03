# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874090.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11874090
#
# ASCII decay Descriptor: [[B0] ==> mu+ nu_mu (D*- -> (D~0 -> K+ pi-) pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11874090
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Xmunu,D0=cocktail,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
