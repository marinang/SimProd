# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144007.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11144007
#
# ASCII decay Descriptor: {[[B0]nos -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)0 -> K+ pi-)]cc, [[B0]os -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11144007
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKst,mm=LargeLifetime.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B0H  99998  510  0.0  5.27953000  2e-011  B0H  0   0.000000e+000", "B0L  99999  150  0.0  5.27953000  2e-011  B0L  0   0.000000e+000" ]
