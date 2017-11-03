# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42321000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 42321000
#
# ASCII decay Descriptor: pp -> [W+ -> e+ nu_e]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wenue.py" )
from Configurables import Generation
Generation().EventType = 42321000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_enue.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
