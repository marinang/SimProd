# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11134001.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11134001
#
# ASCII decay Descriptor: {[ B0 -> (eta_c(1S) -> p+ p~-) K+ pi-]CC}
#
from Configurables import Generation
Generation().EventType = 11134001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etacKpi,pp=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[ B0 -> ( eta_c(1S) => ^p+ ^p~- ) ^K+ ^pi- ]CC'
tightCut.Cuts      =    {
    '[B0]cc'   : ' goodB  ' , 
    '[p+]cc'   : ' goodProton  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    'eta_c(1S)' : ' goodEtac ',
    '[pi+]cc'   : ' goodPion  ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'goodProton  = ( GPT > 250  * MeV ) & inAcc' , 
    'goodKaon  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPion  = ( GPT > 150  * MeV ) & inAcc' ,
    'goodEtac  = in_range( 1.8, GY, 4.5)' ,
    'goodB  = ( GCTAU > 0.1e-3 * ns * c_light)' ]


