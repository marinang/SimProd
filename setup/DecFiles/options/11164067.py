# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164067.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11164067
#
# ASCII decay Descriptor: {[[B0]nos => pi+ pi- (D~0 -> pi+ pi-)]cc, [[B0]os => pi- pi+ (D0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164067
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pipi,pipi=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
