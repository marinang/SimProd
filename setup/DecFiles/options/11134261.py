# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11134261.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11134261
#
# ASCII decay Descriptor: [B0 -> K+ pi- (h_c -> (eta_c -> p+ anti-p-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11134261
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_hcKpi,pp=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^([ B0 -> ^K+ ^ pi- ^(h_c(1P) -> ^gamma ^(eta_c(1S) -> ^p+ ^p~-) ) ]CC)'
tightCut.Cuts      =    {
    '[B0]cc'   : ' goodB  ' , 
    '[p+]cc'   : ' goodProton  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    '[pi+]cc'    : ' goodPion  ' , 
    'gamma'     : ' goodPhoton ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
    'goodProton  = ( GPT > 250  * MeV ) & inAcc' , 
    'goodKaon  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPion  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPhoton  = ( GPT > 150  * MeV ) & inAcc & inEcalX & inEcalY ' ,
    'goodB  = ( GCTAU > 0.1e-3 * ns * c_light)' ]


