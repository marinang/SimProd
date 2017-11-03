# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114049.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11114049
#
# ASCII decay Descriptor: { B0 -> (Higgs0 -> mu+ pi-) mu+ pi-, B~0 -> (Higgs0 -> mu- pi+) mu- pi+ }
#
from Configurables import Generation
Generation().EventType = 11114049
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_MuPiMajoranaNeutrino2MuPi,m=3000MeV,t=10ps,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction

ParticlePropertySvc().Particles = [ "H_10 87 25 0.0000 3.0000 1.0000e-11 Higgs0 25 0.0000" ]
ApplicationMgr().ExtSvc += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"]
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]

