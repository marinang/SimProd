# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/32113001.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 32113001
#
# ASCII decay Descriptor: [ Sigma+ -> mu+ mu- p+ ]cc
#
from Configurables import Generation
Generation().EventType = 32113001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma+_pmumu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]
