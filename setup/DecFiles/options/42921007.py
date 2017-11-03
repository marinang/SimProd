# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42921007.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 42921007
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> b b~) ...
#
from Configurables import Generation
Generation().EventType = 42921007
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Wbb_lnul,bb=1l,5Gev,2b,powheg.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"

Generation().SampleGenerationTool = "Special"
from Configurables import Special, PowhegProductionWbb, Pythia8Production
Generation().addTool( Special )
Generation().Special.ProductionTool = "PowhegProductionWbb"
Generation().Special.addTool( PowhegProductionWbb () )
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

