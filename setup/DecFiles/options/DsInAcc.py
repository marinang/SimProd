# Extra options to ask J/psi and  Psi(2S) to be in acceptance
from Configurables import Generation, SignalRepeatedHadronization, ListOfDaughtersInLHCb
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( ListOfDaughtersInLHCb ) 
Generation().SignalRepeatedHadronization.SelectedDaughterInLHCb.SelectedPIDs = [ 431 , -431 ]
