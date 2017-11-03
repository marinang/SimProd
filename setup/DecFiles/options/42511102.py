# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42511102.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 42511102
#
# ASCII decay Descriptor: pp -> [W+gamma -> e+ nu_e gamma]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wgammaenu.py" )
from Configurables import Generation
Generation().EventType = 42511102
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Wgamma_enue.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
