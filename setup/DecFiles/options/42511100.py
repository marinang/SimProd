# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42511100.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 42511100
#
# ASCII decay Descriptor: pp -> [W+gamma -> mu+ nu_mu gamma]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wgammamunu.py" )
from Configurables import Generation
Generation().EventType = 42511100
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Wgamma_munumu.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
