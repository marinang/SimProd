# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42300001.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 42300001
#
# ASCII decay Descriptor: pp -> [W+ -> tau+ nu_tau -> anti-nu_tau mu+ nu_mu]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wtaunu=Mu.py" )
from Configurables import Generation
Generation().EventType = 42300001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_taunutau=Mu.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
