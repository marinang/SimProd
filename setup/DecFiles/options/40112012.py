# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40112012.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 40112012
#
# ASCII decay Descriptor: pp -> (A1 -> mu mu) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/A1mumu_fixedWidth.py" )
from Configurables import Generation
Generation().EventType = 40112012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/A1_mumu=7GeV_fixedWidth.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 2
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 1*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.MotherOfLepton = ["H_30"]
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_30 89 36 0.0 7.0 5.485e-21 A0 36 7.0" ]
