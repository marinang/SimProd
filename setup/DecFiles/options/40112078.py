# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40112078.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 40112078
#
# ASCII decay Descriptor: pp -> (H_10 -> mu+ mu-) + b bbbar
#
from Configurables import Generation
Generation().EventType = 40112078
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Hbb=mH32GeV,width10MeV,inAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HbbinAcc"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 32.0 6.582e-023 Higgs0 25 0.0e+00" ]

from Configurables import Generation
from Gaudi.Configuration import *
Generation().PileUpTool = "FixedLuminosityForRareProcess"
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )
from Configurables import Special, Pythia8Production
Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
            "SpaceShower:rapidityOrder = off", 
            "HiggsSM:gg2Hbbbar  = on",
            "25:mWidth = 0.01", 
            "25:mMin =0.0"
            "25:m0 = 32.0",             
            "25:doForceWidth = on",
            "25:onMode = off", 
            "25:onIfAny = 13", 
            "PartonLevel:FSR=on" 
        ]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HbbinAcc" )
tracksInAcc = Generation().HbbinAcc
tracksInAcc.Code = "( (count ( isGoodMuFromH ) > 1) & (count(isGoodBJet) > 1))"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMu = ( ( 'mu+' == GABSID ) & ( GTHETA < 400.0*mrad ) )"
   , "isFromH  = ( 1 == GNINTREE( 'H_10' == GABSID , 0 ) )"
   , "isGoodMuFromH = ( isGoodMu & isFromH )"
   , "isGoodBJet = ( ( 'b' == GABSID  ) & ( GTHETA < 400.0*mrad ) )" ]

