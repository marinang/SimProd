# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15102250.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 15102250
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ pi- gamma]cc
#
from Configurables import Generation
Generation().EventType = 15102250
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_gamma_ppi=HighPtGamma,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " ( count ( isGoodB ) > 0 ) "
radCut.Preambulo += [
		   "from GaudiKernel.SystemOfUnits import GeV, mrad",
		   "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT > 1.5*GeV))",
		   "isGoodB    = (GBEAUTY & NGoodGamma & GDECTREE('[Lambda_b0 -> p+ pi- gamma]CC'))"
		   ]

