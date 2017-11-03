# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14873607.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14873607
#
# ASCII decay Descriptor: { [B_c+ => (J/psi(1S) => mu+ mu-) (D+ --> mu+ ...)]CC, [B_c+ => (J/psi(1S) => mu+ mu-) (D*+ --> mu+ ...)]CC, [B_c+ => (J/psi(1S) => mu+ mu-) (D_s+ --> mu+ ...)]CC, [B_c+ => (J/psi(1S) => mu+ mu-) (D_s*+ --> mu+ ...)]CC }
#
from Configurables import Generation
Generation().EventType = 14873607
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDx,mm,muX=JpsiLeptonInAcceptance.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.ChargedThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.ChargedThetaMax = 10.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
Generation().FullGenEventCutTool = "JpsiLeptonInAcceptance"

from Configurables import JpsiLeptonInAcceptance
Generation().addTool( JpsiLeptonInAcceptance )
Generation().JpsiLeptonInAcceptance.JpsiLepPMin = 0
Generation().JpsiLeptonInAcceptance.BachLepPMin = 0
Generation().JpsiLeptonInAcceptance.PreselMass = False
Generation().JpsiLeptonInAcceptance.PreselDoca = False

