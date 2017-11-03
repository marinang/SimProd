# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15204011.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15204011
#
# ASCII decay Descriptor: [ Lambda_b0 -> p+ K- pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15204011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKpipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ 
 ###                    GEANTID   PDGID   CHARGE   MASS(GeV)       TLIFE(s)             EVTGENNAME           PYTHIAID   MAXWIDTH
 "N(1520)0              404        1214   0.0      1.52000000      5.723584e-24              N(1520)0        0          0.00",
 "N(1520)~0             405       -1214   0.0      1.52000000      5.723584e-24         anti-N(1520)0        0          0.00",
]

