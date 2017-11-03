# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28194071.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 28194071
#
# ASCII decay Descriptor: psi(3770) -> D0(K- pi+)  D0bar(K+ pi-)
#
from Configurables import Generation
Generation().EventType = 28194071
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/psi3770_D0D0bar,Kpi=TightCuts.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 30443 ]

from Configurables import LoKi__GenCutTool as GenCutTool

Generation().SignalPlain.addTool( GenCutTool , 'TightCut' )
Generation().SignalPlain.TightCut.Decay = ' ^( psi(3770) -> ^( D0 =>  ^K- ^pi+)  ^(D~0 => ^K+ ^pi- ) )'
Generation().SignalPlain.TightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import GeV',
    'inAcc         = in_range ( 0.010 , GTHETA , 0.400 )',
    'goodPion      = (GP > 4.5 * GeV) & (GPT > 0.55 * GeV) & inAcc',
    'goodKaon      = (GP > 4.5 * GeV) & (GPT > 0.55 * GeV) & inAcc',
    'goodPsiDaugD  = (GNINTREE ( ( 421 == GABSID ) & ( GPT > 1.4 * GeV ) , 1 ) > 0.5 )'
    ]
Generation().SignalPlain.TightCut.Cuts = {
    '[pi+]cc'       : 'goodPion ',
    '[K+]cc'        : 'goodKaon ',
    '[psi(3770)]cc' : 'goodPsiDaugD '
    }

