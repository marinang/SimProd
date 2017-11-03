from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCbAndWithDaughAndBCuts
from GaudiKernel.SystemOfUnits import MeV

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithDaughAndBCuts ) 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackPT = 250*MeV 
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinMuonPT = 250*MeV
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithDaughAndBCuts.MinTrackP = 2000*MeV
