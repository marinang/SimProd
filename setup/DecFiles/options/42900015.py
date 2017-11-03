# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42900015.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 42900015
#
# ASCII decay Descriptor: pp -> (Z0 -> c c~) + mu+ mu-
#
from Configurables import Generation
Generation().EventType = 42900015
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_cc,2mu,inAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Z_cc2muinAcc"

from Configurables import Generation
from Gaudi.Configuration import *
Generation().PileUpTool = "FixedLuminosityForRareProcess"
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )
from Configurables import Special, Pythia8Production
Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
            "WeakSingleBoson:ffbar2gmZ = on", #Z0/gamma* production                                                    
            "WeakBosonAndParton:qg2gmZq = on", #q g -> Z q
            "WeakBosonAndParton:qqbar2gmZg = on", #q qbar -> Z g
            "WeakBosonAndParton:ffbar2gmZgm = on" # Z + gamma
            "WeakBosonAndParton:fgm2gmZf = on" # Z + lepton 
            "WeakDoubleBoson:ffbar2gmZgmZ = on" #double Z0/gamma*
            "WeakDoubleBoson:ffbar2ZW  = on" #ZW
            "WeakZ0:gmZmode = 2", #Z0 only
            "23:onMode = off", #turn it off
            "23:onIfAny = 4" #turn on decay to c quarks
        ]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "Z_cc2muinAcc" )
tracksInAcc = Generation().Z_cc2muinAcc
tracksInAcc.Code = "( (count ( isGoodCFromZ ) > 1) & (count(isGoodMuPlus) > 0) & (count(isGoodMuMinus) > 0))"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMuPlus = ( ( 'mu+' == GID ) & ( GTHETA < 400.0*mrad ) & (GPT > 2.5*GeV))"
   , "isGoodMuMinus = ( ( 'mu-' == GID ) & ( GTHETA < 400.0*mrad ) & (GPT > 2.5*GeV))"
   , "isGoodC = ( ( 'c' == GABSID ) & ( GTHETA < 400.0*mrad ) )"
   , "isFromZ  = ( 1 == GNINTREE( 'Z0' == GABSID , 0 ) )"
   , "isGoodCFromZ = ( isGoodC & isFromZ )" ]

