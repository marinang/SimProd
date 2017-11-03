# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14147090.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 14147090
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (J/psi(1S) -> mu+ mu-) pi+ pi+ pi- ) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Bc2sVegPyOpts.py" )
from Configurables import Generation
Generation().EventType = 14147090
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc2_Bcpipi,Jpsipipipi,mm=DecProdCut,BcVegPy,BC_VHAD.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_c+ 77 541 1.0 6.85800000 1.017330e-20 B_c+ 541 0.0003", "B_c- 78 -541 -1.0 6.85800000 1.017330e-20 B_c- -541 0.0003", "B+ 71 521 1.0  6.27400000   5.090000e-13  B+ 521 0.00000000", "B- 72 -521 -1.0  6.27400000   5.090000e-13 B- -521 0.00000000" ]
