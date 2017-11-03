from Configurables import (Generation, Special, Pythia8Production)
from GaudiKernel import SystemOfUnits
from Gaudi.Configuration import importOptions

Generation().PileUpTool = "FixedNInteractions"
Generation().DecayTool = ''
# Special options.
Generation().addTool(Special)
Generation().Special.CutTool = ''
Generation().Special.DecayTool = ''
Generation().Special.ProductionTool = 'Pythia8Production'

# Pythia8 options.
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    # Turn on all hard light QCD production.
    'HardQCD:gg2gg = on',
    'HardQCD:gg2qqbar = on',
    'HardQCD:qg2qg = on',
    'HardQCD:qq2qq = on',
    'HardQCD:qqbar2gg = on',
    'HardQCD:qqbar2qqbarNew = on',
    'PhaseSpace:pTHatMin = 20',
    # Allow Pythia to handle QED radiation (switch off if using PHOTOS).
    "ParticleDecays:allowPhotonRadiation = on"
    ]
