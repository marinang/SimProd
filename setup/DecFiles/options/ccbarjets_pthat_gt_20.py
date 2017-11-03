# Pythia options for hard scatter exclusive ccbar with pthat>20GeV
# The purpose of this is to use as a sample to measure selection
# efficiencies on c-jets and NOT to estimate yields from ccbar as
# important contributions from flavour excitation and gluon splitting
# are missing
from Configurables import Generation
from Gaudi.Configuration import *
Generation().PileUpTool = "FixedLuminosityForRareProcess";

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 0",
    "pysubs msub 81 1",
    "pysubs msub 82 1",
    "pypars mstp 7  4",
    "pysubs ckin 3 20",
    "pysubs ckin 4 -1",
    ]


