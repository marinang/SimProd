# Options to configure instance called DStarZeroCut of LoKi::GenCutTool
# @author Zenwhei Yang
# @date   2011.08.17
#
from Configurables import Generation, SignalPlain, DStarZeroCut, ToolSvc, GenFactory

Generation().addTool( SignalPlain )
Generation().SignalPlain.addTool( DStarZeroCut ) 
Generation().SignalPlain.DStarZeroCut.Decay = " [ ( D*(2007)0 -> ^( D0 => ^K- ^pi+) ^gamma ) || ( D*(2007)0 -> ^( D0 => ^K- ^pi+) ( pi0 -> ^gamma  ^gamma ) ) ]CC "
Generation().SignalPlain.DStarZeroCut.Cuts = [
  '[K+]cc'   : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 200 * MeV ) " ,
  '[pi+]cc'  : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 200 * MeV ) " ,
  '[D0]cc'   : "                                      ( GPT >   5 * GeV ) " ,
  'gamma'    : " in_range( 400 * MeV , GPT  , 5 * GeV   ) & ( in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ) ) " ]

Generation().SignalPlain.DStarZeroCut.Preambulo = [
   "from LoKiCore.functions import in_range"  ,
   "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
]

Generation().SignalPlain.DStarZeroCut.Factory =  "LoKi::Hybrid::GenTool/GenFactory:PUBLIC"
ToolSvc().addTool( GenFactory ) 
ToolSvc().GenFactory.Modules = [ "LoKiGen.decorators" ]
