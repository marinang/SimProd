# Extra options for J/psi to be in acceptance

from Configurables import Generation, SignalRepeatedHadronization, SelectedDaughterInLHCb

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( SelectedDaughterInLHCb ) 
Generation().SignalRepeatedHadronization.SelectedDaughterInLHCb.SelectedPIDs = [ 443 ]
