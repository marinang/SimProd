# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102424.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11102424
#
# ASCII decay Descriptor: {[[B0]nos -> K+ K- (pi0 -> gamma gamma)]cc, [[B0]os -> K- K+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102424
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-pi0=TightCuts,sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[^(B0 => ^K+ ^K- ^(pi0 -> ^gamma ^gamma))]CC'
tightCut.Cuts      =    {
    '[B0]cc'    : ' goodB     ' , 
    '[K+]cc'    : ' goodTrack ' , 
    'pi0'       : ' goodPi0   ' ,
    'gamma'     : ' goodGamma ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodB     = ( GPT > 2500 * MeV )                ' , 
    'goodTrack = ( GPT >  495 * MeV ) & inAcc        ' , 
    'goodPi0   = ( GPT >  800 * MeV )                ' , 
    'goodGamma = ( GPZ > 0 ) & inEcalX & inEcalY     ' ]


