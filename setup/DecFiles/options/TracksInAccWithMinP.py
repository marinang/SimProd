# Extra options to apply min momentum cuts on daughters
from Configurables import Generation
from Gaudi.Configuration import *
from GaudiKernel.SystemOfUnits import MeV

from Configurables import SignalRepeatedHadronization, DaughtersInLHCbAndWithMinP
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndWithMinP )
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndWithMinP.MinTrackP = 1600.0*MeV

from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.addTool( DaughtersInLHCbAndWithMinP )
Generation().SignalPlain.DaughtersInLHCbAndWithMinP.MinTrackP = 1600.0*MeV



