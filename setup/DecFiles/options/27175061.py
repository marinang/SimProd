# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27175061.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 27175061
#
# ASCII decay Descriptor: [D_s1(2536)+ -> (D_s+ -> K+ K- pi+) mu+ mu- ]cc
#
from Configurables import Generation
Generation().EventType = 27175061
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds1_Dsmumu,KKpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 10433,-10433 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D_s1(2536)+           173       10433   1.0      2.53510000      7.154480e-22                    D'_s1+       10433      0.005", "D_s1(2536)-           177      -10433  -1.0      2.53510000      7.154480e-22                    D'_s1-      -10433      0.005" ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s1(2536)+ => ^(D_s+ => ^K+ ^K- ^pi+ ) ^mu+ ^mu- ]CC'
tightCut.Cuts      =    {
    '[K+]cc'         : ' goodKaon ' , 
    '[pi+]cc'        : ' goodPion ' , 
    '[mu+]cc'        : ' goodMuon ' } 

tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodMuon   = inAcc' ] 


