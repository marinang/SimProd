# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11876000.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11876000
#
# ASCII decay Descriptor: [B0 -> (D_s*+ -> (D_s+ -> (phi -> K+ K-) pi+) gamma) (D*- -> (anti-D0 -> K+ mu- anti-nu_mu ) pi- )]cc
#
from Configurables import Generation
Generation().EventType = 11876000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDst,phipiDpi,KKmunuX=cocktail,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
