# @file
#  Options to include to produce beam gas in VeLo region providing
#  generic beam and vertex conditions, according to acceptance for
#  Beam 2.
#
#  @author G. Corti
#  @date   2010-07-07
#
 
# Settings for pp "fixed target", single interactions
from Configurables import Generation, MinimumBias, PythiaProduction, FlatZSmearVertex
from GaudiKernel.SystemOfUnits import m

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction ) 
Generation().MinimumBias.PythiaProduction.BeamToolName = "FixedTarget"
Generation().PileUpTool = "FixedNInteractions"
 
# Settings for flat smaring of primary vertex in z
Generation().VertexSmearingTool = "FlatZSmearVertex"
Generation().addTool( FlatZSmearVertex ) 
Generation().FlatZSmearVertex.ZMin = -0.5*m
Generation().FlatZSmearVertex.ZMax = 2.0*m
