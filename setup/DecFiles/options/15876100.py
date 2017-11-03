# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15876100.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15876100
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) mu+ nu_mu) (D- -> pi- pi- K+)]cc
#
from Configurables import Generation
Generation().EventType = 15876100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcD,DmunuX=cocktail,DmuInAcc.dec"
Generation().SignalPlain.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import Generation, Generation, ListOfDaughtersInLHCb
Generation().SignalPlain.addTool( ListOfDaughtersInLHCb )
Generation().SignalPlain.ListOfDaughtersInLHCb.DaughtersPIDList = [ 411 , 13 ]


