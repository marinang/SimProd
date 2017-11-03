# Pythia options for W->taunu 42300002
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [ 
    # Turn on W production.
    "pysubs msel 12",
    # Allow only W decays with taus.
    "pydat3 mdme 190 1 0",
    "pydat3 mdme 191 1 0",
    "pydat3 mdme 192 1 0",
    "pydat3 mdme 193 1 0",
    "pydat3 mdme 194 1 0",
    "pydat3 mdme 195 1 0",
    "pydat3 mdme 196 1 0",
    "pydat3 mdme 197 1 0",
    "pydat3 mdme 198 1 0",
    "pydat3 mdme 199 1 0",
    "pydat3 mdme 200 1 0",
    "pydat3 mdme 201 1 0",
    "pydat3 mdme 202 1 0",
    "pydat3 mdme 203 1 0",
    "pydat3 mdme 204 1 0",
    "pydat3 mdme 205 1 0",
    "pydat3 mdme 206 1 0",
    "pydat3 mdme 207 1 0",
    "pydat3 mdme 208 1 1",
    "pydat3 mdme 209 1 0",
    # Allow only tau decays with electrons.
    "pydat3 mdme 89  1 1",
    "pydat3 mdme 90  1 0",
    "pydat3 mdme 91  1 0", 
    "pydat3 mdme 92  1 0", 
    "pydat3 mdme 93  1 0", 
    "pydat3 mdme 94  1 0", 
    "pydat3 mdme 95  1 0", 
    "pydat3 mdme 96  1 0", 
    "pydat3 mdme 97  1 0", 
    "pydat3 mdme 98  1 0", 
    "pydat3 mdme 99  1 0", 
    "pydat3 mdme 100 1 0",
    "pydat3 mdme 101 1 0",
    "pydat3 mdme 102 1 0",
    "pydat3 mdme 103 1 0",
    "pydat3 mdme 104 1 0",
    "pydat3 mdme 105 1 0",
    "pydat3 mdme 106 1 0",
    "pydat3 mdme 107 1 0",
    "pydat3 mdme 108 1 0",
    "pydat3 mdme 109 1 0",
    "pydat3 mdme 110 1 0",
    "pydat3 mdme 111 1 0",
    "pydat3 mdme 112 1 0",
    "pydat3 mdme 113 1 0",
    "pydat3 mdme 114 1 0",
    "pydat3 mdme 115 1 0",
    "pydat3 mdme 116 1 0",
    "pydat3 mdme 117 1 0",
    "pydat3 mdme 118 1 0",
    "pydat3 mdme 119 1 0",
    "pydat3 mdme 120 1 0",
    "pydat3 mdme 121 1 0",
    "pydat3 mdme 122 1 0",
    "pydat3 mdme 123 1 0",
    "pydat3 mdme 124 1 0",
    "pydat3 mdme 125 1 0",
    "pydat3 mdme 126 1 0",
    "pydat3 mdme 127 1 0",
    "pydat3 mdme 128 1 0",
    "pydat3 mdme 129 1 0",
    "pydat3 mdme 130 1 0",
    "pydat3 mdme 131 1 0",
    "pydat3 mdme 132 1 0",
    "pydat3 mdme 133 1 0",
    "pydat3 mdme 134 1 0",
    "pydat3 mdme 135 1 0",
    "pydat3 mdme 136 1 0",
    "pydat3 mdme 137 1 0",
    "pydat3 mdme 138 1 0",
    "pydat3 mdme 139 1 0",
    "pydat3 mdme 140 1 0",
    "pydat3 mdme 141 1 0",
    "pydat3 mdme 142 1 0"
    ]

Generation().Special.Pythia8Production.Commands += [
    # Turn on W production.
    "WeakSingleBoson:ffbar2W = on",
    # Allow only W decays with taus.
    "24:onMode = off",
    "24:onIfMatch = -15 16",
    # Allow only tau decays with electrons.
    "15:onMode = off",
    "15:onIfMatch = 16 11 -12",
    # Allow Pythia to handle QED radiation (switch off if using PHOTOS).
    "ParticleDecays:allowPhotonRadiation = on"
    ]

Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType ) 
Generation().Special.PythiaHiggsType.MotherOfLepton = [ "tau+" ]
Generation().Special.PythiaHiggsType.TypeOfLepton = [ "e+" ]
# Allow Pythia to handle tau decays (not EvtGen through TAUOLA).
Generation().Special.DecayTool = ""
