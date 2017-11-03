# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11244203.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11244203
#
# ASCII decay Descriptor: [B0 ->  ( [ chi_c1(1P) , chi_c2(1P)] -> (J/psi(1S) -> mu+ mu-) gamma ) ( K*(892) => K+ pi- ) ]cc
#
from Configurables import Generation
Generation().EventType = 11244203
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_chicKst,JpsigKpi,mm=TightCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ B0 ->  ( Meson -> ^( J/psi(1S) => ^mu+ ^mu-) ^gamma ) ( K*(892)0 => ^K+ ^pi-) ]CC'
tightCut.Cuts      =    {
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    '[pi+]cc'   : ' goodPion  ' , 
    'J/psi(1S)' : ' goodPsi   ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' , 
    'goodKaon  = ( GPT > 150  * MeV )                        & inAcc   ' , 
    'goodPion  = ( GPT > 150  * MeV )                        & inAcc   ' , 
    'goodGamma = ( 0 < GPZ ) & ( 150 * MeV < GPT ) & inEcalX & inEcalY ' ,
    'goodPsi   = ( GPT > 500  * MeV ) & in_range ( 1.8 , GY , 4.5 )    ' ]


