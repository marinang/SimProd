# Extra options to apply cuts solely on charged particles, so no cuts on neutrals

# Note: the cuts are applied as follows
#       particle does not pass if fabs( sin( angle ) ) > fabs( sin( NeutralThetaMax ) )
#       particle does not pass if fabs( sin( angle ) ) < fabs( sin( NeutralThetaMin ) )
from Configurables import Generation, SignalRepeatedHadronization, DaughtersInLHCb

Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCb )
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMin = 0 
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMax = 3.14159265358979323846/2
