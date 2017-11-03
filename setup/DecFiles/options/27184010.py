# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27184010.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 27184010
#
# ASCII decay Descriptor: [D*0 -> (D0 -> K- pi+) e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 27184010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst0_D0ee,Kpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = '^[D*(2007)0 -> ^(D0 ==> ^K- ^pi+) ^e+ ^e-]CC'
tightCut.Preambulo += [
  'from GaudiKernel.SystemOfUnits import MeV' ,
  'from LoKiCore.functions import in_range',
  ]
tightCut.Cuts = {
  '[D*(2007)0]cc'   : '(GP >  6000 * MeV)',
  '[D0]cc'          : '(GP >  3000 * MeV)',
  '[K-]cc'          : '(GP >  1500 * MeV) & (in_range(0.010, GTHETA, 0.300))',
  '[pi+]cc'         : '(GP >  1500 * MeV) & (in_range(0.010, GTHETA, 0.300))',
  '[e+]cc'          : '(GP >  1500 * MeV) & (in_range(0.010, GTHETA, 0.300))'
  }

