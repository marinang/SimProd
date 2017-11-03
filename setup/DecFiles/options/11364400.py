# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11364400.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11364400
#
# ASCII decay Descriptor: [[B0] -> (D*(2010)- -> (D- ->  pi+ pi- pi- pi0) pi0) pi+ pi- pi+ pi0]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11364400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-3pipi0,3pipi0=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
