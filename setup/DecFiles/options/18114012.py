# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18114012.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 18114012
#
# ASCII decay Descriptor: Upsilon(2S) -> (Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}) pi+ pi-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon2S,Upsilon1Spipi=DecProdCut,fix.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 100553
