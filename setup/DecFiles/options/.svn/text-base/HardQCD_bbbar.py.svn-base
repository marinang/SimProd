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
    # Turn on all bbar hard QCD production.
    'HardQCD:hardbbbar = on',
    'PhaseSpace:pTHatMin = 20',
    # Allow Pythia to handle QED radiation (switch off if using PHOTOS).
    "ParticleDecays:allowPhotonRadiation = on"
    ]
