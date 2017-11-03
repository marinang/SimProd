from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCbAndWithDaughAndBCuts
from GaudiKernel.SystemOfUnits import MeV

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithDaughAndBCuts ) 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackPT = 400*MeV
