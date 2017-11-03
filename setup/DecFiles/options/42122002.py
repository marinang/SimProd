# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42122002.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 42122002
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> e+ e- {,gamma} {,gamma}) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgee=PHOTOS.py" )
from Configurables import Generation
Generation().EventType = 42122002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zg_ee=PHOTOS.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.MotherOfLeptonMinMass = 40*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
