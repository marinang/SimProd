# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15266011.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 15266011
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p K+ pi-) anti-p p+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15266011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacppbarpi=TwoRes,DecProdCut,pCut1600MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "a_4(2040)+ 365 219 1.0 2.5 1.567172e-24 Np+ 219 0.47","a_4(2040)- 366 -219 -1.0 2.5 1.567172e-24 Np- -219 0.47","pi(1800)+ 841 9010211 1.0 3.0 3.0e-24 Np2+ 9010211 0.98","pi(1800)- 842 -9010211 -1.0 3.0 3.0e-24 Np2- -9010211 0.98" ]
