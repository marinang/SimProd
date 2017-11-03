# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16275062.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 16275062
#
# ASCII decay Descriptor: [ Xi_bc+ -> (Lambda_c+ -> p+ K- pi+)  (J/psi -> mu+ mu-) ]cc
#
from Configurables import Generation
Generation().EventType = 16275062
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_bc+"
Generation().Special.GenXiccProduction.Commands = ["mixevnt imix 1", "loggrade ivegasopen 0", "loggrade igrade 1", "vegasbin nvbin 300", "counter xmaxwgt 5000000", "confine pscutmin 0.0", "confine pscutmax 7.0"]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibc_LcJpsi,pKpi-res,mm=DecProdCut,m=6.9GeV,t=0.4ps.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCb"
from Configurables import XiccDaughtersInLHCb
Generation().Special.addTool( XiccDaughtersInLHCb )
Generation().Special.XiccDaughtersInLHCb.BaryonState = Generation().Special.GenXiccProduction.BaryonState
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Xi_bc+ 532 5242 1.0 6.90000000 0.400000e-12 Xi_bc+ 5242 0.00000000", " Xi_bc~- 533 -5242 -1.0 6.90000000 0.400000e-12 anti-Xi_bc- -5242 0.00000000" ]
