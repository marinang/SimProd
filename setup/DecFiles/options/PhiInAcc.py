# Extra options for phi to be in acceptance

from Configurables import Generation, SignalRepeatedHadronization, SelectedDaughterInLHCb

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( SelectedDaughterInLHCb ) 
Generation().SignalRepeatedHadronization.SelectedDaughterInLHCb.SelectedPIDs = [ 333 ]
