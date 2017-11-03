# ============================================================================
# @file
#
#  The main configuration file to run "Hidden Valley multipion production"
#
# Matt Strassler <strasslr@noether.phys.washington.edu> :
#
#  "This program simulates q qbar -> Z' -> v-quarks, followed by
#  v-showering and v-hadronization to v-pions.  The current program
#  makes various approximations and is not suitable for precision studies,
#  but should be good at the factor-of-two level.   In particular,
#  the v-hadronization code uses Pythias QCD hadronization code, scaled
#  up in energy, and this is not a perfect simulation of the real model.
#   Also, the Z' charges are not precisely those discussed in ref [1]; 
#  but in any case the model of [1] was just an example, and many other
#  models exist.  Updates to this program will gradually correct these issues."
#
#  
#  Each concrete file needs to specify the properties of Z',H_20 and H_30
#  separately:
#  
#  @code 
#
#  // include this "common" configuration file:
#  #include "$GAUSSROOT/cmt/HidValley.opts"
#
#  // define the event type 
#  Generation.EventType = 449000<XY> ;
#
#  // define the particular properties of Z', H_20 and H_30 
#  ParticlePropertySvc.Particles = {
#  "H_20 88 35 0.0 120.0 9.4e-26 Higgs'0 35 0.0e+00" ,
#  "H_20 88 35 0.0 120.0 9.4e-26 Higgs'0 35 0.0e+00" ,
#  "H_30 89 36 0.0  40.0 1.0e-12      A0 36 0.0e+00"
#   } ;
#  
#  @endcode 
#
# ===========================================
# "Hidden Valley: multi v-pions production"
# ===========================================
# event type  m(Z')  m(vp0)  t(vpi0) t(vpi+)
# ===========================================
# 44900001    3000    35      100.0ps   inf 
# 44900002    3000    50       10.0ps   inf 
# 44900003    3000    70        1.0ps   inf 
# 44900004    3000   120        0.1ps   10ps  
# ===========================================
#
#  @author Vanya BELYAEV ibelyaev@physics.syr.edu
#  @date 2006-10-20
#/
# ============================================================================
from Configurables import Generation
from Gaudi.Configuration import *

from Configurables import Special, HidValleyProduction
Generation().addTool( Special )
Generation().Special.addTool( HidValleyProduction )

Generation().Special.ProductionTool  = "HidValleyProduction"
Generation().Special.HidValleyProduction.Commands = []
Generation().Special.HidValleyProduction.PyGiveCommands = [
    # General switches 
    # store the documentation strings (?)
  "MSTP(128)=2"  # IMPORTANT to preserve the event history 
]

# select only event with large amount of b-quarks "in-acceptance":
Generation().Special.CutTool     = "NbQuarks"
from Configurables import NbQuarks
Generation.Special.addTool( NbQuarks ) 
Generation.Special.NbQuarks.NB = 3
# use the fixed number of interactions 
Generation().PileUpTool = "FixedNInteractions"

Generation().Special.PileUpProductionTool = ""

from Configurables import Giga, GiGaPhysListModular, GiGaHiggsParticles
giga = GiGa() 

giga.addTool( GiGaPhysListModular( "ModularPL" ) , name = "ModularPL" )
GiGa.ModularPL.PhysicsConstructors += [ "GiGaHiggsParticles" ]
GiGa.ModularPL.addTool( GiGaHiggsParticles ) 
GiGa.ModularPL.GiGaHiggsParticles.Higgses = [ "H_20" , "H_30" ]
