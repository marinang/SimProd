# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11442013.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11442013
#
# ASCII decay Descriptor: {[B0 --> (J/psi(1S) => mu+ mu-) ...]CC}
#
from Configurables import Generation
Generation().EventType = 11442013
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiX,mm,HighMass=JpsiLeptonInAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().FullGenEventCutTool = "JpsiLeptonInAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from GaudiKernel.SystemOfUnits import GeV, mrad, mm
from Configurables import LoKi__GenCutTool
from Configurables import JpsiLeptonInAcceptance

Generation().SignalRepeatedHadronization.addTool(LoKi__GenCutTool,'TightCut')
trackFilters = Generation().SignalRepeatedHadronization.TightCut
trackFilters.Preambulo += [
   'inAccTot  = in_range ( 0, abs(GPT/GPZ), 0.423 )', # abs(theta) < 250 mrad 
   'inAccXZ   = in_range ( 0, abs(GPX/GPZ), 0.423 )', # abs(thetaXZ) < 400 mrad
   'inAccYZ   = in_range ( 0, abs(GPY/GPZ), 0.256 )', # abs(thetaYZ) < 250 mrad 
   'goodMuon  = (GPZ > 0) & (GPT > 300*MeV ) & (GP > 2.9*GeV) & inAccTot & inAccXZ & inAccYZ' , 
   'goodPsi   = (GPT > 1.5*GeV)'
   ]
trackFilters.Decay = "Beauty --> ^( J/psi(1S) => ^mu+ ^mu-) ..."
trackFilters.Cuts = {
   'J/psi(1S)' : 'goodPsi',
   '[mu+]cc' : 'goodMuon'
   }

Generation().addTool( JpsiLeptonInAcceptance )
Generation().JpsiLeptonInAcceptance.JpsiPtMin = 1.950*GeV
Generation().JpsiLeptonInAcceptance.JpsiLepPtMin = 0.525*GeV
Generation().JpsiLeptonInAcceptance.BachLepPtMin = 0.305*GeV
Generation().JpsiLeptonInAcceptance.JpsiLepPMin = 2.9*GeV
Generation().JpsiLeptonInAcceptance.BachLepPMin = 2.9*GeV
Generation().JpsiLeptonInAcceptance.LepMaxHorzTheta = 400*mrad
Generation().JpsiLeptonInAcceptance.LepMaxVertTheta = 250*mrad
Generation().JpsiLeptonInAcceptance.LepMinTheta = 10*mrad
Generation().JpsiLeptonInAcceptance.LepMaxTheta = 400*mrad
Generation().JpsiLeptonInAcceptance.PreselMass = True
Generation().JpsiLeptonInAcceptance.MinMass = 6.45*GeV
Generation().JpsiLeptonInAcceptance.MaxMass = 10.0*GeV
Generation().JpsiLeptonInAcceptance.PreselDoca = True
Generation().JpsiLeptonInAcceptance.DocaCut = 0.3*mm


