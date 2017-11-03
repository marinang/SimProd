# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18912032.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 18912032
#
# ASCII decay Descriptor: Upsilon(4S) -> (Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}) eta'
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon4S.py" )
from Configurables import Generation
Generation().EventType = 18912032
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon4S,Upsilon1Setap=Swave,DecProdCut,fix.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 300553
