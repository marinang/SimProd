# Pythia options for W->taunu 42321000
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production, HerwigppProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )
Generation().Special.addTool( HerwigppProduction )


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
    "pydat3 mdme 209 1 0"
    ]

Generation().Special.Pythia8Production.Commands += [
    # Turn on W production.
    "WeakSingleBoson:ffbar2W = on",
    # Allow only W decays with taus.
    "24:onMode = off",
    "24:onIfMatch = -15 16",
    # Allow Pythia to handle QED radiation (switch off if using PHOTOS).
    "ParticleDecays:allowPhotonRadiation = on"
    ]



Generation().Special.HerwigppProduction.Commands += [
    "cd /Herwig/MatrixElements/",
    "insert SimpleQCD:MatrixElements[0] MEqq2W2ff",
    "set MEqq2W2ff:Wcharge Both",
    "set MEqq2W2ff:Process Tau"
    ]
   


Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType ) 
Generation().Special.PythiaHiggsType.TypeOfLepton = [ "tau+" ]
# Allow Pythia to handle tau decays (not EvtGen through TAUOLA).
Generation().Special.DecayTool = ""
