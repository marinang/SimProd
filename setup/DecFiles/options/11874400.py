# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874400.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11874400
#
# ASCII decay Descriptor: [[B0] ==> mu+ nu_mu (D*- -> (D- -> K+ pi- pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11874400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D+Xmunu,D+=cocktail,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
