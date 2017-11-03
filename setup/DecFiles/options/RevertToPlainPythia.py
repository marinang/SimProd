# Default PYTHIA6.4 options:
from Configurables import Generation
from Gaudi.Configuration import *

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import MinimumBias, PythiaProduction

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction )

Generation().MinimumBias.PythiaProduction.Commands += [ 
  "pysubs ckin 41 12.0" ,
  "pypars mstp 2 1" ,
  "pypars mstp 33 0" ,
  "pypars mstp 128 0" ,
  "pypars mstp 81 1" ,
  "pypars mstp 82 4" ,
  "pypars mstp 52 1" ,
  "pypars mstp 51 7" ,
  "pypars mstp 142 0" ,
  "pypars parp 67 4.0" ,
  "pypars parp 82 2.0" ,
  "pypars parp 89 1800." ,
  "pypars parp 90 0.16" ,
  "pypars parp 85 0.9" ,
  "pypars parp 86 0.95" ,
  "pypars parp 91 2.0" ,
  "pypars parp 149 1.0" ,
  "pypars parp 150 1.0" ,
  "pydat1 parj 11 0.5" ,
  "pydat1 parj 12 0.6" ,
  "pydat1 parj 13 0.75" ,
  "pydat1 parj 14 0.0" ,
  "pydat1 parj 15 0.0" ,
  "pydat1 parj 16 0.0" ,
  "pydat1 parj 17 0.0" ,
  "pydat1 mstj 26 2" ,
  "pydat1 parj 33 0.8" ,
  "pydat1 mstu 12 0" , 
  "pydat1 mstu 13 1" , 
  "pydat1 mstu 25 1" , 
  "pypars mstp 122 1" 
]
