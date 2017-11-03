# @file
#  Options to include to specify generation in Calorimeter acceptance 
#  for particle guns with automatic generation of options
#  
#  @author G. Corti
#  @date   2006-08-24
#  @date   2008-07-21, adapt to changes in ParticleGun
#/

from Configurables import ParticleGun
from Gaudi.Configuration import *
from GaudiKernel.SystemOfUnits import rad

from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange ) 
ParticleGun().MomentumRange.ThetaMin = 0.037*rad
ParticleGun().MomentumRange.ThetaMax = 0.240*rad

from Configurables import GenInit, SimInit, GaudiSequencer
GenInit( "GaussGen" ).PrintFreq = 100
SimInit( "GaussSim" ).PrintFreq = 100

if "GiGaGetEventAlg" in GaudiSequencer("SimMonitor").Members:
    GaudiSequencer("SimMonitor").Members.remove("GiGaGetEventAlg")
