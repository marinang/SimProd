# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41900010.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 41900010
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> b b~) ...
#
from Configurables import Generation
Generation().EventType = 41900010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tt_bb=1l,10GeV,2b,powheg.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"

Generation().SampleGenerationTool = "Special"
from Configurables import Special, PowhegProductiontt, Pythia8Production
Generation().addTool( Special )
Generation().Special.ProductionTool = "PowhegProductiontt"
Generation().Special.addTool( PowhegProductiontt () )
Generation().Special.PowhegProductiontt.topdecaymode = "02000"
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsTypeCut" )
tracksInAcc = Generation().HiggsTypeCut
tracksInAcc.Code = " ((count ( isGoodLeptonW ) >0) & (count ( isGoodBeauty)>1)) "
tracksInAcc.Preambulo += [                                                                        
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                           
    , "isGoodLeptonW     = ((  'W+' == GABSID ) & GINTREE( GLEPTON & ( GTHETA < 350.0*mrad ) & (GPT > 10*GeV)))"
    , "isGoodBeauty   = ((  'b' == GABSID ) & GINTREE( GBEAUTY & ( GTHETA < 350.0*mrad ) & (GPT > 0*GeV)))"
   ]      
Generation().Special.PileUpProductionTool = "Pythia8Production"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
Generation().Special.addTool( Pythia8Production () )
Generation().Special.ReinitializePileUpGenerator = False
Generation().Special.Pythia8Production.Tuning = "LHCbDefault.cmd"

