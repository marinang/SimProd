# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15874020.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15874020
#
# ASCII decay Descriptor: {[Lb_b0 => (Lb_c+ ->p+  K- pi+)  nu_mu mu+]cc}, Lc(2625)+ Intermediate state only
#
from Configurables import Generation
Generation().EventType = 15874020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,Lc2625,pKpi=cocktail.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
