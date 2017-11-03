# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166105.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11166105
#
# ASCII decay Descriptor: [B0 ->  (D*(2010)- -> (anti-D0 -> (K_S0 -> pi+ pi-) (K_S0 -> pi+ pi-))  pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166105
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstPi,D0pi,KsKs=TightCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B0 -> ^(D*(2010)- -> ^(D~0 => ^(KS0 ==> ^pi+ ^pi-) ^(KS0 ==> ^pi+ ^pi-)) pi-) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.010, GTHETA, 0.300))',
    'goodB        = (GP > 7500 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.105 * millimeter)',
    'goodD     = ( GP > 10 * GeV ) & switch(GCHILD(GPT,1) < GCHILD(GPT,2), (GCHILD(GPT,1) > 300) & (GCHILD(GPT,2) > 800), (GCHILD(GPT,1) > 800) & (GCHILD(GPT,2) > 300)) & inAcc            ' , 
    'goodDst     = ( GP > 20 * GeV ) & (GCHILD(GTHETA,2) > 0.01) & (GCHILD(GTHETA,2) < 0.3)     ' , 
    'goodKS   = ( GP >  4 * GeV) & inAcc & (GFAEVX( abs( GVZ  ) , 0 ) < 2500 * mm) & (GCHILD(GPT,1) > 100 * MeV) &  (GCHILD(GPT,2) > 100 * MeV) &  (GCHILD(GP,1) > 2.0 * GeV) &  (GCHILD(GP,2)  > 2.0 * GeV)        ' 
]
tightCut.Cuts      =    {
    '[D*(2010)+]cc'  : 'goodDst',
    '[D0]cc'         : 'goodD',
    '[KS0]cc'        : 'goodKS',
    }

