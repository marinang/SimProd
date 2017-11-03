# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114024.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11114024
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (rho0 -> pi+ pi-)]cc, [[B0]os -> mu- mu+ (rho0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114024
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhomumu=MSC10wrong,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
