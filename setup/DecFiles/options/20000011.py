# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/20000011.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 20000011
#
# ASCII decay Descriptor: pp => [<Xc>]cc ...
#
from Configurables import Generation
Generation().EventType = 20000011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_c,powheg.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twocinAcc"

Generation().SampleGenerationTool = "Special"
from Configurables import Special, PowhegProductioncc, Pythia8Production
Generation().addTool( Special )
Generation().Special.ProductionTool = "PowhegProductioncc"
Generation().Special.addTool( PowhegProductioncc () )
Generation().Special.PowhegProductioncc.qmass =  1.5
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twocinAcc" )
tracksInAcc = Generation().twocinAcc
tracksInAcc.Code = " (count ( isGoodC)>1) "
tracksInAcc.Preambulo += [                                                                        
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                           
    , "isGoodC   = ((  'c' == GABSID ) & GINTREE( GCHARM & ( GTHETA < 350.0*mrad ) & (GPT > 0*GeV) ))"
   ]      
Generation().Special.PileUpProductionTool = "Pythia8Production"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
Generation().Special.addTool( Pythia8Production () )
Generation().Special.ReinitializePileUpGenerator = False
Generation().Special.Pythia8Production.Tuning = "LHCbDefault.cmd"

