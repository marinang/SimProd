# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10074000.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 10074000
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10074000
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=DMuInCascade.dec"
Generation().Inclusive.CutTool = "DMuCascadeInAcc"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]
