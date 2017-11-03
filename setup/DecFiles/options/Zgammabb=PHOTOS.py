# Pythia options for Zgamma->bb for 42100200
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
  "PartonLevel:FSR=off",
  "SpaceShower:rapidityOrder = off", #pT ordering!
  "WeakBosonAndParton:ffbar2gmZgm = on", #f f -> Z gamma
  "WeakZ0:gmZmode = 2",
  "23:onMode = off", #Turn Z decays
  "23:onIfAny = 5" #Turn on bbar decay
  ]

def appendPhotos():
  from Configurables import ApplyPhotos
  GaudiSequencer( "GeneratorSlotMainSeq" ).Members += [ ApplyPhotos( ) ]
  ApplyPhotos().PDGId = [ 23 ] 
  
appendPostConfigAction(appendPhotos)
