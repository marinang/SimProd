# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104522.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11104522
#
# ASCII decay Descriptor: [B0 -> (eta -> pi+ pi- pi0) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104522
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etaKs,pi+pi-pi0=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SampleGenerationTool="SignalRepeatedHadronization"
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = 'B0 -> ^(eta -> ^pi+ ^pi- ^pi0) ^(KS0 -> ^pi+ ^pi-)'
tightCut.Cuts      =    {
    '[B0]cc'       : ' goodB     ' , 
    '[KS0]cc'      : ' goodKS    ' ,
    '[pi+]cc'      : ' goodTrack ' ,
    '[eta]cc'      : ' goodEta   ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GPT > 1500 * MeV ) ' ,
    'goodKS    = ( GPT > 1200 * MeV ) ' ,
    'goodEta   = ( GPT > 2000 * MeV ) ' ,
    'goodTrack = ( GPT > 300 * MeV ) & inAcc ' ]


