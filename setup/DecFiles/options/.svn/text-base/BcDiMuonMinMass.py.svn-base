from Configurables import Generation, Special, BcDaughtersInLHCbAndMassCut
from GaudiKernel.SystemOfUnits import MeV

Generation().addTool( Special )
Generation().Special.addTool( BcDaughtersInLHCbAndMassCut ) 

Generation().Special.BcDaughtersInLHCbAndMassCut.PreselMinMass = True
Generation().Special.BcDaughtersInLHCbAndMassCut.mmMinMass = 4500*MeV
Generation().Special.BcDaughtersInLHCbAndMassCut.PreselMaxMass = False
Generation().Special.BcDaughtersInLHCbAndMassCut.PreselDausPT = False
