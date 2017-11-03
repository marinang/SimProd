# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22104112.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 22104112
#
# ASCII decay Descriptor: [D0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 22104112
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KSKS=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
#gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
#tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[^(D0 ==> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-))]CC'
tightCut.Cuts      =    {
    '[D0]cc'    : ' goodB     ' , 
    'KS0'   : ' goodKs ' , 
    '[pi+]cc'   : ' goodTrack ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.000 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GP > 10 * GeV )   & inAcc            ' , 
    'goodTrack = ( GP >  1.5 * GeV )        ' , 
    'goodKs   = ( GP >  3 * GeV) & (GPT >  100 * MeV ) & inAcc              ' ] 


