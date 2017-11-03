# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42921001.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 42921001
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WZlnulbb.py" )
from Configurables import Generation
Generation().EventType = 42921001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WZ_lnul,bb.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 0
Generation().Special.PythiaHiggsType.MotherOfThebquarks = "Z0"
