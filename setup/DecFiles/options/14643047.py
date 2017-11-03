# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14643047.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14643047
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) => mu+ mu-) (tau+ => mu+ nu_mu nu_tau~) nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 14643047
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,mununu=BcVegPy,ffKiselev.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
