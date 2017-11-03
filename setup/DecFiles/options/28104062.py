# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28104062.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 28104062
#
# ASCII decay Descriptor: eta_c(1S) -> ( phi(1020) -> K+ K- ) ( phi(1020) -> K+ K- )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/etac.py" )
from Configurables import Generation
Generation().EventType = 28104062
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_etac,phiphi=Pt0.3GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 441 ]
 
from Configurables import LoKi__GenCutTool as GenCutTool 
#
Generation().SignalPlain.addTool( GenCutTool , 'TightCut' ) 
Generation().SignalPlain.TightCut.Decay = "eta_c(1S) => ^( phi(1020) => ^K+ ^K-) ^( phi(1020) => ^K+ ^K- )"
Generation().SignalPlain.TightCut.Cuts = {
    'K+' : ' ( GPT > 0.3 * GeV ) & inAcc ',
    'K-' : ' ( GPT > 0.3 * GeV ) & inAcc '
    }
Generation().SignalPlain.TightCut.Preambulo += [
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 ) '
    ]

