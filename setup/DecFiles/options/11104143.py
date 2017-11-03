# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104143.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11104143
#
# ASCII decay Descriptor: [B0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104143
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSKS=DecProdCut,tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[^(B0 ==> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-))]CC'
tightCut.Cuts      =    {
    '[B0]cc'    : ' goodB     ' , 
    'KS0'   : ' goodKs ' , 
    '[pi+]cc'   : ' goodTrack ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.000 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GP > 15 * GeV )   & inAcc            ' , 
    'goodTrack = ( GP >  1.6 * GeV )       ' , 
    'goodKs   = ( GP >  4 * GeV) & (GPT >  300 * MeV ) & inAcc              ' ] 


