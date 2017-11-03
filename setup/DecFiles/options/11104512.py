# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104512.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11104512
#
# ASCII decay Descriptor: [B0 -> (eta' -> (eta -> gamma gamma) pi+ pi-) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104512
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKs,etapipi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SampleGenerationTool="SignalRepeatedHadronization"
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = 'B0 -> ^(eta_prime -> ^(eta -> ^gamma ^gamma ) ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-)'
tightCut.Cuts      =    {
    '[B0]cc'       : ' goodB     ' , 
    '[KS0]cc'      : ' goodKS    ' ,
    '[pi+]cc'      : ' goodTrack ' ,
    '[eta_prime]cc': ' goodEtap  ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GPT > 1500 * MeV ) ' ,
    'goodKS    = ( GPT > 1200 * MeV ) ' ,
    'goodEtap  = ( GPT > 2000 * MeV ) ' ,
    'goodTrack = ( GPT > 300 * MeV ) & inAcc ' ]


