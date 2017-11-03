# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42971000.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 42971000
#
# ASCII decay Descriptor: pp -> [W+ -> mu+ nu_mu]cc +c-jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wmunucjet.py" )
from Configurables import Generation
Generation().EventType = 42971000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_munucjet.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
