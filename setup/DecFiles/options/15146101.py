# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15146101.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 15146101
#
# ASCII decay Descriptor: [Lambda_b0 -> (J/psi(1S) -> mu+ mu-) (KS0 -> pi+ pi-) (Lambda0 -> p+ pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15146101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiKsLambda,mm=DecProdCut,pCut1600MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
