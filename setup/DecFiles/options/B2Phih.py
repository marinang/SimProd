from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCbAndWithDaughAndBCuts
from GaudiKernel.SystemOfUnits import MeV, GeV

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithDaughAndBCuts ) 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackPT = 800*MeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackP = 8*GeV
