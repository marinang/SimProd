# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11676000.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11676000
#
# ASCII decay Descriptor: {[[B0]nos->nu_mu mu+ (D*(2010)- -> pi- (D~0 => K+ pi- pi+ pi-))]cc,[[B0]os -> anti_nu_mu mu- (D*(2010)+ -> pi+ (D0 => K- pi+ pi- pi+))]cc}
#
from Configurables import Generation
Generation().EventType = 11676000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,Kpipipi=hqet,MINT.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
