# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16203032.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16203032
#
# ASCII decay Descriptor: [ Xi_b- -> p+ K- pi- ]cc
#
from Configurables import Generation
Generation().EventType = 16203032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_pKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]


from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ 
 ###                    GEANTID   PDGID   CHARGE   MASS(GeV)       TLIFE(s)             EVTGENNAME           PYTHIAID   MAXWIDTH
 "N(1520)0              404        1214   0.0      1.52000000      5.723584e-24              N(1520)0        0          0.00",
 "N(1520)~0             405       -1214   0.0      1.52000000      5.723584e-24         anti-N(1520)0        0          0.00",
]

