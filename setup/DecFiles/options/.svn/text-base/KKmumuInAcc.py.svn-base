# Extra options to ask J/psi and  Phi to be in acceptance

from Configurables import Generation, SignalRepeatedHadronization, ListOfDaughtersInLHCb
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( ListOfDaughtersInLHCb )
Generation().SignalRepeatedHadronization.ListOfDaughtersInLHCb.DaughtersPIDList = [ 321 , -321 , 13 , -13 ]
