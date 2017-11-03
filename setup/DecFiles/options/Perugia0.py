from Configurables import Generation
from Gaudi.Configuration import *

importOptions( "$DECFILESROOT/options/RevertToPlainPythia.py" )

from Configurables import MinimumBias, PythiaProduction

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( PythiaProduction )

Generation().MinimumBias.PythiaProduction.Commands += [
  "pypars mstp 0" ,
  "pysubs msub 11 1" ,
  "pysubs msub 12 1" ,
  "pysubs msub 13 1" ,
  "pysubs msub 28 1" ,
  "pysubs msub 53 1" ,
  "pysubs msub 68 1" ,
  "pysubs msub 91 1" ,
  "pysubs msub 92 1" ,
  "pysubs msub 93 1" ,
  "pysubs msub 94 1" ,
  "pysubs msub 95 1" ,
  "pysubs msub 421 1" ,
  "pysubs msub 422 1" ,
  "pysubs msub 423 1" ,
  "pysubs msub 424 1" ,
  "pysubs msub 425 1" ,
  "pysubs msub 426 1" ,
  "pysubs msub 427 1" ,
  "pysubs msub 428 1" ,
  "pysubs msub 429 1" ,
  "pysubs msub 430 1" ,
  "pysubs msub 431 1" ,
  "pysubs msub 432 1" ,
  "pysubs msub 433 1" ,
  "pysubs msub 434 1" ,
  "pysubs msub 435 1" ,
  "pysubs msub 436 1" ,
  "pysubs msub 437 1" ,
  "pysubs msub 438 1" ,
  "pysubs msub 439 1" ,
  "pysubs msub 461 1" ,
  "pysubs msub 462 1" ,
  "pysubs msub 463 1" ,
  "pysubs msub 464 1" ,
  "pysubs msub 465 1" ,
  "pysubs msub 466 1" ,
  "pysubs msub 467 1" ,
  "pysubs msub 468 1" ,
  "pysubs msub 469 1" ,
  "pysubs msub 470 1" ,
  "pysubs msub 471 1" ,
  "pysubs msub 472 1" ,
  "pysubs msub 473 1" ,
  "pysubs msub 474 1" ,
  "pysubs msub 475 1" ,
  "pysubs msub 476 1" ,
  "pysubs msub 477 1" ,
  "pysubs msub 478 1" ,
  "pysubs msub 479 1" ,
  "pypars mstp 5 320" 
]
