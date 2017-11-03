# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11266021.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11266021
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2010)- -> (D~0 -> K+ pi-) pi-) K+ pi- pi+]cc, [[B0]os -> ( D*(2010)+ -> (D0 => K- pi+) pi+) K- pi+ pi-]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11266021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-Kpipi,D0pi-,Kpi=DecProdCut_pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
