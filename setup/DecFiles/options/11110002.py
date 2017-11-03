# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11110002.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11110002
#
# ASCII decay Descriptor: [B0 -> (tau+ -> pi+ pi- pi+ anti-nu_tau) (tau- -> mu- anti-nu_mu nu_tau)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11110002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_tautau,mu3pi=DecProdCut,TightCut,tauolacleo.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
