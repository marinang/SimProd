# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41900004.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 41900004
#
# ASCII decay Descriptor: pp => (t => b ...) (t~ => b~ ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Top.py" )
from Configurables import Generation
Generation().EventType = 41900004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tt_bb=1l,5GeV,1b.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 5*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 1
Generation().Special.PythiaHiggsType.MotherOfThebquarks = "t"
