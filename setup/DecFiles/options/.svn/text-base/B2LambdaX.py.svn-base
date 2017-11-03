from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCbAndWithDaughAndBCuts
from GaudiKernel.SystemOfUnits import MeV, GeV

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithDaughAndBCuts ) 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinLongLivedDaughPT = 200*MeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackPT = 200*MeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinLongLivedDaughP = 1*GeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackP = 1*GeV
