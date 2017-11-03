# Pythia options for Z->cc 42900002
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [ 
                                                     "WeakSingleBoson:ffbar2gmZ = on", #Z0/gamma* production                                                    
                                                     "WeakBosonAndParton:qg2gmZq = on", #q g -> Z q
                                                     "WeakBosonAndParton:qqbar2gmZg = on", #q qbar -> Z g
                                                     "WeakBosonAndParton:ffbar2gmZgm = on" # Z + gamma
                                                     "WeakBosonAndParton:fgm2gmZf = on" # Z + lepton 
                                                     "WeakDoubleBoson:ffbar2gmZgmZ = on" #double Z0/gamma*
                                                     "WeakDoubleBoson:ffbar2ZW  = on" #ZW
                                                     "WeakZ0:gmZmode = 2", #Z0 only
                                                     "23:onMode = off", #turn it off
                                                     "23:onIfAny = 4" #turn on decay to b quarks
                                                     ]
