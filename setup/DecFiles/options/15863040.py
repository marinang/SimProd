# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15863040.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 15863040
#
# ASCII decay Descriptor: [ Lambda_b0 ->  (Lambda_c+ -> p+ K- pi+)  (tau- -> pi- pi+ pi- pi0 nu_tau) anti-nu_tau   ]cc
#
from Configurables import Generation
Generation().EventType = 15863040
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lctaunu,pKpi=cocktail,tau3pipi0,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
from Configurables import DaughtersInLHCb
Generation().SignalPlain.addTool( DaughtersInLHCb )
Generation().SignalPlain.DaughtersInLHCb.NeutralThetaMin = 0.
Generation().SignalPlain.DaughtersInLHCb.NeutralThetaMax = 10.
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
