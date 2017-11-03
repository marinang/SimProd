# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11514010.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11514010
#
# ASCII decay Descriptor: {[B0 -> (tau- -> pi- pi- pi+ nu_tau) mu+]cc, [B_s0 -> (tau+ -> pi- pi+ pi+  anti-nu_tau ) mu-]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11514010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_mutau,pipipinu=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
