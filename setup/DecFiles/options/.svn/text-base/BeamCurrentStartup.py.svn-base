# @file
#  Options to include to scale Beam gas in LSS or Arc 
#  with machine not yet conditioned with beam current as in
#  Startup, i.e. 1/3 of p/bunch with 2808 bunches or nominal
#  bunch intensity (1.15 x 10^11 p/bunch) with 756 bunches. 
#  This is the expected conditions in 2009.
#
#  @author G. Corti
#  @date   2008-07-30
#

from Configurables import MIBackground, Beta10StartupBeam1Muons, Beta10StartupBeam1Hadrons, Beta10StartupBeam2Muons, Beta10StartupBeam2Hadrons

MIBackground().addTool( Beta10StartupBeam1Muons )
MIBackground().addTool( Beta10StartupBeam1Hadrons )
MIBackground().addTool( Beta10StartupBeam2Muons )
MIBackground().addTool( Beta10StartupBeam2Hadrons ) 

MIBackground().Beta10StartupBeam1Muons.ScalingFactor = 0.33
MIBackground().Beta10StartupBeam1Hadrons.ScalingFactor = 0.33
MIBackground().Beta10StartupBeam2Muons.ScalingFactor = 0.33
MIBackground().Beta10StartupBeam2Hadrons.ScalingFactor = 0.33
