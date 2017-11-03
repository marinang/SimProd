# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166050.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11166050
#
# ASCII decay Descriptor: [[([B0]os => ^(D0 -> ^pi+ ^pi- ^pi+ ^pi-) ^(K*(892)~0 -> ^K- ^pi+))]CC, [([B0]nos => ^(D~0 -> ^pi+ ^pi- ^pi+ ^pi-) ^(K*(892)0 -> ^K+ ^pi-))]CC]
#
from Configurables import Generation
Generation().EventType = 11166050
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst,pipipipi=B-SVS,D-PHSP,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[Beauty-> ^(D~0 => ^pi+ ^pi- ^pi+ ^pi-) ^(K*(892)0 =>^K+ ^pi-) ]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'goodB0       = (GP > 50000 * MeV) & (GPT > 5000 * MeV) & (GTIME > 0.105 * millimeter)',
   'goodD0       = (GP > 20000 * MeV) & (GPT >  300 * MeV)',
   'goodKst      = (GP > 12000 * MeV) & (GPT >  800 * MeV)',
   'goodDDaugPi  = (GNINTREE( ("pi+"==GABSID) & (GP > 1000 * MeV) & inAcc, 1) > 3.5)',
   'goodKstPi  = (GNINTREE( ("pi+"==GABSID) & (GP > 2000 * MeV) & (GPT > 98 * MeV) & inAcc, 1) > 0.5)',
   'goodKstK   = (GNINTREE( ("K+"==GABSID) & (GP > 2000 * MeV) & (GPT > 98 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts = {
   'Beauty'          : 'goodB0', 
   '[D0]cc'          : 'goodD0 & goodDDaugPi',
   '[K*(892)0]cc'    : 'goodKst & goodKstPi & goodKstK',
   }

