# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14873610.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 14873610
#
# ASCII decay Descriptor: { [B_c+ -> (D_s*+ -> (D_s+ -> eta mu+ nu_mu) gamma) (J/psi -> mu+ mu-)]cc }
#
from Configurables import Generation
Generation().EventType = 14873610
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiCharm2Body,mm,muX=JpsiLeptonInAcceptance.dec"
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

