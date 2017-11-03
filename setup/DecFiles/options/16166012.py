# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16166012.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 16166012
#
# ASCII decay Descriptor: [Sigma_b0 -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 16166012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lbstar5920_Lbpipi,Lcpi=DecProdCut_pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b0   112   5212  0.0  5.920000  1.000000e-019       Sigma_b0   5212  1.000000e-004", " Sigma_b~0  113  -5212  0.0  5.920000  1.000000e-019  anti-Sigma_b0  -5212  1.000000e-004" ]
