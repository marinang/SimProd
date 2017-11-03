from Configurables import Generation, MinimumBias, Pythia8Production
from Gaudi.Configuration import *

Generation().addTool( MinimumBias )
Generation().MinimumBias.addTool( Pythia8Production ) 

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" ) 

Generation().MinimumBias.Pythia8Production.Commands += [
  "SoftQCD:singleDiffractive = on",
  "SoftQCD:doubleDiffractive = on"
]
