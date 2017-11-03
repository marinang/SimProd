# Extra options to ask J/psi and  Psi(2S) to be in acceptance

from Configurables import Generation, SignalRepeatedHadronization, SelectedDaughterInLHCb
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( SelectedDaughterInLHCb ) 
Generation().SignalRepeatedHadronization.SelectedDaughterInLHCb.SelectedPIDs = [ 443 , 100443 ]

from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.addTool( SelectedDaughterInLHCb ) 
Generation().SignalPlain.SelectedDaughterInLHCb.SelectedPIDs = [ 443 , 100443 ]
