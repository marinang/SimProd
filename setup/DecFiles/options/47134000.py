# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/47134000.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 47134000
#
# ASCII decay Descriptor: pp => ( J/psi(1S) -> mu+ mu ) ( J/psi(1S) -> mu+ mu- ) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/LbOniaPsi1S1S.py" )
from Configurables import Generation
Generation().EventType = 47134000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "OniaPairsProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_JpsiJpsi,mmmm=GluonFusion,FullGenEventCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/PsiPairInAcc"
 
from Configurables import OniaPairsProduction
Generation().Special.addTool( OniaPairsProduction )
from Gaudi.Configuration import *
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "PsiPairInAcc" )
Generation().PsiPairInAcc.Code = " count ( isPsi & inY & isGood ) > 1.5 "
Generation().PsiPairInAcc.Preambulo += [
    "isPsi         = ( 'J/psi(1S)' == GID ) " , 
    "inY           = in_range ( 2. , GY , 4.5 ) " , 
    "FromGluFusion = ( ~GHAS( ('cluster' == GID) | ('string' == GID) , HepMC.ancestors ) ) " , 
    "notFromB     = 0 == GNINTREE ( GBEAUTY , HepMC.ancestors ) " , 
    "isGood        = ( 3 != GSTATUS ) & FromGluFusion & notFromB "
    ]

