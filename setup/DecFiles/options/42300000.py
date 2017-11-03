# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42300000.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 42300000
#
# ASCII decay Descriptor: pp -> [W+ -> tau+ nu_tau]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wtaunu.py" )
from Configurables import Generation
Generation().EventType = 42300000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_taunutau.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
