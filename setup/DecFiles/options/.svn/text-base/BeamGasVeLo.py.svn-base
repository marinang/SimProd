# @file
#  Options to include to produce beam gas in VeLo region providing
#  generic beam and vertex conditions at 7.0 TeV 
#
#  @author D. Gregori, G. Corti
#  @date   2006-06-21
#
 
# Settings for pp "fixed target", single interactions
from Configurables import Generation, MinimumBias, PythiaProduction
from GaudiKernel.SystemOfUnits import m

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction ) 
Generation().MinimumBias.PythiaProduction.BeamToolName = "FixedTarget"
Generation().PileUpTool = "FixedNInteractions"
 
# Settings for flat smaring of primary vertex in z
from Configurables import FlatZSmearVertex
Generation().VertexSmearingTool = "FlatZSmearVertex"
Generation().addTool( FlatZSmearVertex ) 
Generation().FlatZSmearVertex.ZMin = -2.0*m
Generation().FlatZSmearVertex.ZMax = 2.0*m
 
