# $Id:$
#  ============================================================================
## @file LbOniaPSi1S1S.py
#  Congfigurtaion file with extra-options
#  to run production of J/psi pairs
#  @see OniaPAirsProduction
#  ============================================================================


# these 2 lines are needed due to ordering problem
#  ["ExtraOptions" is included before Special&Production tools are added]
#  Actually they are later duplicated with automatically generated options 
from Configurables import Generation, Special, OniaPairsProduction
Generation()        .addTool( Special ) 
Generation().Special.addTool( OniaPairsProduction )


#
from Configurables import Generation, Gauss
from GaudiKernel   import SystemOfUnits
#
Generation().Special.OniaPairsProduction.Ecm = 2 * Gauss().BeamMomentum / SystemOfUnits.GeV
## direct 2xJ/psi    producton 
Generation().Special.OniaPairsProduction.Psi1S1S = 1
## direct J/psi+psi' producton 
Generation().Special.OniaPairsProduction.Psi1S2S = 1
## direct 2xpsi'     producton 
Generation().Special.OniaPairsProduction.Psi2S2S = 1

# =============================================================================
# The END
# =============================================================================
