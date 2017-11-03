# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15674313.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15674313
#
# ASCII decay Descriptor: [Lambda_b0 => (D*_s- -> (D_s- -> K+ K- pi-) gamma) (Lambda_c+ -> Lambda0 nu_mu mu+)]cc
#
from Configurables import Generation
Generation().EventType = 15674313
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_DsstLcX,DsgammamunuX,KKpi=cocktail,mu3hInAcc.dec"
Generation().SignalPlain.CutTool = "BeautyTo2CharmTomu3h"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
