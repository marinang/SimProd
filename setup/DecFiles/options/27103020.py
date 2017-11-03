# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27103020.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 27103020
#
# ASCII decay Descriptor: [D*_s+ -> K+ K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 27103020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dsst_KKpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 433,-433 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[D*_s+ => ^K- ^K+ ^pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )               ' ,
    'fastTrack    =  ( GPT > 200 * MeV ) & ( GP  > 1.9 * GeV )         ' , 
    'goodTrack    =  inAcc &  fastTrack                                ' ,     
    'goodDs       =  ( GPT > 0.9 * GeV )         ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )            ' , 
    'notFromB     =  0 == Bancestors                                   ' 
]

tightCut.Cuts     =    {
    '[D*_s+]cc': 'goodDs & notFromB ' ,
    '[K+]cc'  : 'goodTrack ' , 
    '[pi+]cc' : 'goodTrack '
    }

