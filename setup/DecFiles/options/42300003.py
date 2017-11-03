# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42300003.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 42300003
#
# ASCII decay Descriptor: pp -> [W+ -> tau+ nu_tau -> anti-nu_tau pi+ pi+ pi-]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wtaunu=PimPimPip.py" )
from Configurables import Generation
Generation().EventType = 42300003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_taunutau=PimPimPip.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
