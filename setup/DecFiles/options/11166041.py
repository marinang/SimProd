# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166041.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11166041
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) (a_1+ -> (anti-K*0 -> K- pi+) K+ )]cc, [[B0]os -> (D+ => K- pi+ pi+) (a_1- -> (K*0 -> K+ pi-) K- )]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11166041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Da1,Kpipi,KKpi=DecProdCut,pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
