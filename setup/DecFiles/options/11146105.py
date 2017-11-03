# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11146105.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11146105
#
# ASCII decay Descriptor: [B0 -> (eta -> pi+ pi- gamma) (KS0 -> pi+ pi-) (J/psi(1S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11146105
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKseta,mm,pi+pi-g=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
