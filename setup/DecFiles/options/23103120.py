# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23103120.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 23103120
#
# ASCII decay Descriptor: [Ds+->(K*0->(KS0->pi+pi-)pi+)]cc
#
from Configurables import Generation
Generation().EventType = 23103120
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_Kst0pi+_Kst2Kspi0=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
