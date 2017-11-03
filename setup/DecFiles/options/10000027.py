# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10000027.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 10000027
#
# ASCII decay Descriptor: pp -> [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10000027
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b,powheg.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twobinAcc"

Generation().SampleGenerationTool = "Special"
from Configurables import Special, PowhegProductionbb, Pythia8Production
Generation().addTool( Special )
Generation().Special.ProductionTool = "PowhegProductionbb"
Generation().Special.addTool( PowhegProductionbb () )
Generation().Special.PowhegProductionbb.qmass =  4.75
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twobinAcc" )
tracksInAcc = Generation().twobinAcc
tracksInAcc.Code = " (count ( isGoodB)>1) "
tracksInAcc.Preambulo += [                                                                        
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                           
    , "isGoodB   = ((  'b' == GABSID ) & GINTREE( GBEAUTY & ( GTHETA < 350.0*mrad ) & (GPT > 0*GeV)))"
   ]      
Generation().Special.PileUpProductionTool = "Pythia8Production"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
Generation().Special.addTool( Pythia8Production () )
Generation().Special.ReinitializePileUpGenerator = False
Generation().Special.Pythia8Production.Tuning = "LHCbDefault.cmd"

