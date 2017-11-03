# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14113000.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14113000
#
# ASCII decay Descriptor: [B_c+ ->  (Higgs0 -> mu+ pi-) mu+]cc
#
from Configurables import Generation
Generation().EventType = 14113000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_MuMajoranaNeutrino2MuPi,m=3000MeV,t=10ps,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction

ParticlePropertySvc().Particles = [ "H_10 87 25 0.0000 3.0000 1.0000e-11 Higgs0 25 0.0000" ]
ApplicationMgr().ExtSvc += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"] # H_10, H_20, H_30
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]

