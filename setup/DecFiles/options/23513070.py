# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23513070.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 23513070
#
# ASCII decay Descriptor: [D_s+ -> pi+ pi- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23513070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pipimu+nu_mu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
