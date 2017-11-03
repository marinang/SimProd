# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104151.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15104151
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (phi(1020) -> K+ K-)]CC
#
from Configurables import Generation
Generation().EventType = 15104151
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdaPhi,LambdaTopK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi__GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import Generation, SignalPlain, LoKi__GenCutTool
from LoKiCore.functions import in_range
from GaudiKernel.SystemOfUnits import GeV, MeV
from Configurables import LoKi__GenCutTool

gen = Generation()
gen.addTool( SignalPlain )
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
TightCut = gen.SignalPlain.TightCut
TightCut.Decay = '[^(Lambda_b0 -> (Lambda0 => ^p+ ^pi-) (phi(1020) => ^K+ ^K-))]CC'
TightCut.Preambulo += [
    'AccCut     = in_range ( 0.005 , GTHETA , 0.400 )' ]
TightCut.Cuts      =    {
    '[p+]cc'    : ' AccCut ' ,
    '[pi-]cc'   : ' AccCut ' ,
    '[K+]cc'    : ' AccCut ' ,
    '[Lambda_b0]cc'    : ' GPT>1250*MeV ' }

