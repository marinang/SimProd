from Configurables import Generation
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/RevertToPlainPythia.py" )

from Configurables import MinimumBias, PythiaProduction

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction )

Generation().MinimumBias.PythiaProduction.Commands += [ 
  "pysubs msel 1" ,
  "pypars mstp 5 129" 
]
