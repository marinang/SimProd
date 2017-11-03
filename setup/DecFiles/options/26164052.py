# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26164052.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 26164052
#
# ASCII decay Descriptor: [Xi_cc++ -> (D+ -> K- pi+ pi+ ) p+ ]cc
#
from Configurables import Generation
Generation().EventType = 26164052
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc++"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc++_D+p,Kpipi=GenXicc,DecProdCut,WithMinPT,Fix.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
from GaudiKernel import SystemOfUnits
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.MinXiccPT = 2000*SystemOfUnits.MeV
