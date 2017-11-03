# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26168160.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 26168160
#
# ASCII decay Descriptor: [ Xi_cc++ -> ( Xi_c+ -> ( Xi- -> ( Lambda0 -> p+ pi- ) pi+ ) pi+ pi+ ) pi+ pi- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 26168160
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc++"
Generation().Special.GenXiccProduction.Commands = ["mixevnt imix 1", "loggrade ivegasopen 0", "loggrade igrade 1", "vegasbin nvbin 300", "counter xmaxwgt 5000000", "confine pscutmin 0.0", "confine pscutmax 7.0"]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc++_Xic+pipipi,Xipipi=DecProdCut,WithMinPT.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState


GenXiccListOfCommands = [ 
  "subopen ichange 1"
 ,"upcom pmb 1.85"
 ,"upcom pmc 1.85"
]
Generation().Special.addTool( GenXiccProduction , name = "GenXiccProduction" )
Generation().Special.GenXiccProduction.Commands += GenXiccListOfCommands

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [
### The mass of Xi_cc++ can not be set here. The value 3.7 is just for consistency.
###                  GEANTID       PDGID  CHARGE      MASS(GeV)        TLIFE(s)               EVTGENNAME    PYTHIAID        MAXWIDTH
    "Xi_cc++             506        4422     2.0            3.7       4.50e-013                  Xi_cc++        4422   0.000000e+000",
    "Xi_cc~--            507       -4422    -2.0            3.7       4.50e-013             anti-Xi_cc--       -4422   0.000000e+000"
]


