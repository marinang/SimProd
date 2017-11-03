from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCbAndWithDaughAndBCuts
from GaudiKernel.SystemOfUnits import GeV

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithDaughAndBCuts ) 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackPT = 1.*GeV 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinBPT = 1.1*GeV 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackP = 2.7*GeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinBP = 14*GeV
