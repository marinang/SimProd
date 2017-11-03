# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574200.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11574200
#
# ASCII decay Descriptor: [B0 -> (D- -> pi- (eta ->  pi+ pi- gamma)) mu+ nu_mu ]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DmuInAcc.py" )
from Configurables import Generation
Generation().EventType = 11574200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,etapi,pipig=DecProdCut,DmuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
