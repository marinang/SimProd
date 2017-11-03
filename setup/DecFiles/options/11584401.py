# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11584401.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11584401
#
# ASCII decay Descriptor: [B0 -> (D- -> pi- (pi0 -> e+ e- gamma)) mu+ nu_mu ]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DmuInAcc.py" )
from Configurables import Generation
Generation().EventType = 11584401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,pi+pi0,eeg=DmuInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
