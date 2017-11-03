# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15166030.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 15166030
#
# ASCII decay Descriptor: [Lambda_b0 -> (D+ -> K- pi+ pi+) p+ pi- pi-]cc
#
from Configurables import Generation
Generation().EventType = 15166030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dp2pi,K2pi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

 
from Configurables import LoKi__GenCutTool 
from Gauss.Configuration import *
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = '^[Lambda_b0 ==> (D+ ==> ^K- ^pi+ ^pi+) ^p+ ^pi- ^pi-]CC'
tightCut.Preambulo += [
   'from GaudiKernel.SystemOfUnits import millimeter,micrometer,MeV,GeV',
   'inAcc       = in_range ( 0.005 , GTHETA , 0.400 )' ,
   'inEta       = in_range ( 1.85  , GETA   , 5.050 )' ,
   'inY         = in_range ( 1.9   , GY     , 4.6   )' ,
   'goodProton  = ("p+"  == GABSID ) & ( GPT > 0.38 * GeV ) & ( GP  > 8.0 * GeV ) & inAcc & inEta ', 
   'goodKaon    = ("K+"  == GABSID ) & ( GPT > 0.18 * GeV ) & ( GP  > 2.5 * GeV ) & inAcc & inEta ',
   'goodPion    = ("pi+" == GABSID ) & ( GPT > 0.18 * GeV ) & ( GP  > 2.5 * GeV ) & inAcc & inEta ',   
   'goodLambda_b0   =  ( GTIME > 0.05 * millimeter ) &   (GPT > 2.5 * GeV) & inY ',
]
tightCut.Cuts      =    {
    '[p+]cc'        : 'goodProton'   ,
    '[K+]cc'        : 'goodKaon'     , 
    '[pi+]cc'       : 'goodPion'     ,
    '[Lambda_b0]cc' : 'goodLambda_b0'}


