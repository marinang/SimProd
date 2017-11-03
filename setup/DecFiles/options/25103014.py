# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103014.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 25103014
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 25103014
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_pphi,KK=TightCut,Lifetime6.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]

from Configurables import LoKi__GenCutTool as GenCutTool

Generation().SignalPlain.addTool( GenCutTool , 'TightCut' )
Generation().SignalPlain.TightCut.Decay = "[Lambda_c+ => ^p+ ^(phi(1020) => ^K+ ^K-)]CC"
Generation().SignalPlain.TightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns, GeV, mrad, millimeter',
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 )',
    'goodLc    = (GPT > 3.9 * GeV) & (GTIME > 0.0006 * ns) & in_range( 2.0 , GY , 4.5 )',
    'goodProton = (GP > 9.9 * GeV)'
    ]
Generation().SignalPlain.TightCut.Cuts = {
    '[p+]cc'        : 'goodProton & inAcc',
    '[K+]cc'        : 'inAcc',
    '[Lambda_c+]cc' : 'goodLc'
    }

