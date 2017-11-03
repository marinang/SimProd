# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103050.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 25103050
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 25103050
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/LcpKpi3piFromBIncl=DecProdCut_generator_cuts.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndCutsForLc3pi"
from Configurables import DaughtersInLHCbAndCutsForLc3pi
Generation().SignalPlain.addTool( DaughtersInLHCbAndCutsForLc3pi )
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForLc3pi.LcPtCuts = 1.500*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForLc3pi.DaughtersPtMinCut = 150*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForLc3pi.DaughtersPtMaxCut = 150*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForLc3pi.DaughtersPMinCut = 1.00*SystemOfUnits.GeV
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
