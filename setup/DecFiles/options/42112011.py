# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42112011.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 42112011
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> mu+ mu-) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DrellYanmumu10GeV.py" )
from Configurables import Generation
Generation().EventType = 42112011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DrellYan_mumu=10GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 1.0*SystemOfUnits.GeV
