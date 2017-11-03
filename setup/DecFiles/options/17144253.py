# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17144253.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 17144253
#
# ASCII decay Descriptor: [B_s1(L)0 -> (B_s0 -> (J/psi(1S) -> mu+ mu- ) (phi(1020) -> K+ K-)) gamma]cc
#
from Configurables import Generation
Generation().EventType = 17144253
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bsprime1_Bsgamma,Jpsiphi,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.7660000 0.658000e-021 B_s10 10533 0.005000", "B_s1(L)~0 215 -10533 0.0 5.7660000 0.658000e-021 anti-B_s10 -10533 0.005000" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalRepeatedHadronization
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '[B_s1(L)0 => (B_s0 => (J/psi(1S) => ^mu+ ^mu- ) (phi(1020) => ^K+ ^K-)) ^gamma]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )               ' ,
    'fastTrack    =  ( GPT > 200 * MeV ) & ( GP  > 1.9 * GeV )         ' , 
    'goodTrack    =  inAcc &  fastTrack                                ' ,
    'goodPhoton   = ( GPT > 0.25  * GeV ) & inAcc'     
]

tightCut.Cuts     =    {
    '[K+]cc'  : 'goodTrack ' , 
    '[mu+]cc' : 'goodTrack ' ,
    'gamma'   : 'goodPhoton'
    }

