# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18412432.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 18412432
#
# ASCII decay Descriptor: Upsilon(4S) -> (Upsilon(1S) -> mu+ mu- {,gamma} {,gamma}) (eta -> pi+ pi- pi0)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18412432
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilon4S,Upsilon1Seta=Swave,DecProdCut,fix.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 300553
