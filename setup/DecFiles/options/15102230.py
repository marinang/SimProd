# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15102230.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15102230
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1820)0 -> p+ K-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102230
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gammaLambda1820,pK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool( LoKi__GenCutTool, 'TightCut' )

tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = "[Lambda_b0 => (Lambda(1820)0 => p+ K-) ^gamma]CC"
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import GeV"
  , "gammaCut = (GPT > 1.5 * GeV)"
   ]
tightCut.Cuts =   {
  'gamma' : 'gammaCut'
                  }

