# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26266051.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 26266051
#
# ASCII decay Descriptor: [ Xi_cc++ -> (Lambda_c+ -> p K- pi+) K- pi+ pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26266051
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
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc++_LcKpipi,pKpi-res=GenXicc,DecProdCut,WithMinPT3900,MinDaughterPT200.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
from GaudiKernel import SystemOfUnits
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.MinXiccPT = 3900*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.MinDaughterPT = 200*SystemOfUnits.MeV
