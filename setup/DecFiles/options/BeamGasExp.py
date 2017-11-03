# @file
#  Options to include to produce beam gas in experimental beam pipe providing
#  generic beam and vertex conditions at 7.0 TeV 
#
#  @author G. Corti
#  @date   2008-04-29
#
 
# Settings for pp "fixed target", single interactions
from GaudiKernel.SystemOfUnits import m

from Configurables import Generation, MinimumBias, PythiaProduction, FlatZSmearVertex
Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction ) 
Generation().MinimumBias.PythiaProduction.BeamToolName = "FixedTarget"
Generation().PileUpTool = "FixedNInteractions"
 
# Settings for flat smaring of primary vertex in z
Generation().VertexSmearingTool = "FlatZSmearVertex"
Generation().addTool( FlatZSmearVertex ) 
Generation().FlatZSmearVertex.ZMin = -1.9*m
Generation().FlatZSmearVertex.ZMax = 20.0*m
