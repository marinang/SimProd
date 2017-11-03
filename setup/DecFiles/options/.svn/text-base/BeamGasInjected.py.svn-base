# @file
#  Options to include to produce beam gas in VeLo region providing
#  generic beam and vertex conditions at 7.0 TeV 
#
#  @author G. Corti
#  @date   2007-09-27
#
 
# Settings for pp "fixed target", single interactions
from Configurables import Generation, MinimumBias, PythiaProduction
Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction ) 
Generation().MinimumBias.PythiaProduction.BeamToolName = "FixedTarget"
Generation().PileUpTool = "FixedNInteractions"
 
# Settings for uniform smearing of primary vertex in xy and z
Generation().VertexSmearingTool = "UniformSmearVertex" 
