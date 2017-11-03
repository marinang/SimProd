from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [ 
    "pysubs msel 0" ,
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
    "pysubs msub 481 1" ,
    "pysubs msub 482 1" ,
    "pysubs msub 483 1" ,
    "pysubs msub 484 1"
]

Generation().Special.Pythia8Production.Commands += [
    "Bottomonium:all = on"
    ]
