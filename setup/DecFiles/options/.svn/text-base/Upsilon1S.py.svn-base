from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().SignalPlain.PythiaProduction.Commands += [
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

Generation().SignalPlain.Pythia8Production.Commands += [
    "Bottomonium:states(3S1) = 553",
    "Bottomonium:O(3S1)[3S1(1)] = 9.28",
    "Bottomonium:O(3S1)[3S1(8)] = 0.15",
    "Bottomonium:O(3S1)[1S0(8)] = 0.02",
    "Bottomonium:O(3S1)[3P0(8)] = 0.02",
    "Bottomonium:gg2bbbar(3S1)[3S1(1)]g = on",
    "Bottomonium:gg2bbbar(3S1)[3S1(8)]g = on",
    "Bottomonium:qg2bbbar(3S1)[3S1(8)]q = on",
    "Bottomonium:qqbar2bbbar(3S1)[3S1(8)]g = on",
    "Bottomonium:gg2bbbar(3S1)[1S0(8)]g = on",
    "Bottomonium:qg2bbbar(3S1)[1S0(8)]q = on",
    "Bottomonium:qqbar2bbbar(3S1)[1S0(8)]g = on",
    "Bottomonium:gg2bbbar(3S1)[3PJ(8)]g = on",
    "Bottomonium:qg2bbbar(3S1)[3PJ(8)]q = on",
    "Bottomonium:qqbar2bbbar(3S1)[3PJ(8)]g = on"
    ]

Generation().SignalPlain.SignalPIDList = [ 553 ]
