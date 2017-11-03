# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11396400.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11396400
#
# ASCII decay Descriptor: [B0 -> {(D+ -> K- pi+ pi+) || (D+ -> K- K+ pi+)} (D*- -> (pi0,gamma) {(D- -> K+ pi- pi-) || (D- -> K+ K- pi-)})]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11396400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DDst,D-pi0,Kpipi,KKpi=DDALITZ,DecProdCut,pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
