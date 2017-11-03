# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104074.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11104074
#
# ASCII decay Descriptor: [B0 -> p+ p~- pi+ pi-]CC
#
from Configurables import Generation
Generation().EventType = 11104074
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pppipi=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[ B0 -> ^p+ ^p~- ^pi+ ^pi- ]CC'
tightCut.Cuts      =    {
    '[B0]cc'   : ' goodB  ' , 
    '[p+]cc'   : ' goodProton  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    '[pi+]cc'   : ' goodPion  ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'goodProton  = ( GPT > 250  * MeV ) & inAcc' , 
    'goodKaon  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPion  = ( GPT > 150  * MeV ) & inAcc' ,
    'goodB  = ( GCTAU > 0.1e-3 * ns * c_light)' ]


