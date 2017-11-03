# @file
#  Options to include to specify generation in Trackers acceptance 
#  for particle guns with automatic generation of options
#  
#  @author G. Corti
#  @date   2008-07-21
#

from Configurables import ParticleGun
from Gaudi.Configuration import *
from GaudiKernel.SystemOfUnits import rad

from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange ) 
ParticleGun().MomentumRange.ThetaMin = 0.015*rad
ParticleGun().MomentumRange.ThetaMax = 0.300*rad


from Configurables import GenInit, SimInit, GaudiSequencer
GenInit( "GaussGen" ).PrintFreq = 100
SimInit( "GaussSim" ).PrintFreq = 100
# GaudiSequencer( "SimMonitor" ).Members.remove( "GiGaGetEventAlg" )
