from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().SignalPlain.PythiaProduction.Commands += [ "pysubs msel 0" ,
    "pysubs msub 461 0" ,
    "pysubs msub 462 0" ,
    "pysubs msub 463 0" ,
    "pysubs msub 464 0" ,
    "pysubs msub 465 0" ,
    "pysubs msub 466 0" ,
    "pysubs msub 467 0" ,
    "pysubs msub 468 0" ,
    "pysubs msub 469 0" ,
    "pysubs msub 470 0" ,
    "pysubs msub 471 0" ,
    "pysubs msub 473 0" ,
    "pysubs msub 474 0" ,
    "pysubs msub 475 0" ,
    "pysubs msub 476 0" ,
    "pysubs msub 477 0" ,
    "pysubs msub 478 0" ,
    "pysubs msub 479 0" ,
    "pysubs msub 481 0" ,
    "pysubs msub 482 1" ,
    "pysubs msub 483 1" ,
    "pysubs msub 484 1"
]

Generation().SignalPlain.Pythia8Production.Commands += [
    "Bottomonium:states(3S1) = 200553",
    "Bottomonium:O(3S1)[3S1(1)] = 3.54",
    "Bottomonium:O(3S1)[3S1(8)] = 0.075",
    "Bottomonium:O(3S1)[1S0(8)] = 0.1",
    "Bottomonium:O(3S1)[3P0(8)] = 0.1",
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

Generation().SignalPlain.SignalPIDList = [ 200553 ]
