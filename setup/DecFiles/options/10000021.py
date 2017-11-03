# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10000021.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 10000021
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10000021
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=Biased_1DisplVert.dec"
Generation().Inclusive.CutTool = "BiasedBB"
from Configurables import BiasedBB
Generation().Inclusive.addTool( BiasedBB )
Generation().Inclusive.BiasedBB.RadiusMin = 0.4
Generation().Inclusive.BiasedBB.NumberOfBMin = 1
Generation().Inclusive.BiasedBB.EtaMax = 5.0
Generation().Inclusive.BiasedBB.EtaMin = 1.5
Generation().Inclusive.BiasedBB.PtMin = 2.
Generation().Inclusive.BiasedBB.VMin = 0.0
Generation().Inclusive.BiasedBB.CTauMin = 0
Generation().Inclusive.BiasedBB.MinBDeltaPhi = 0
Generation().Inclusive.BiasedBB.MinChargedDaug = 4
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]
