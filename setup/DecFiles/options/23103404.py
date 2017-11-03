# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23103404.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 23103404
#
# ASCII decay Descriptor: [D_s+ -> (phi -> K+ K-) (rho+ -> pi+ pi0)]cc
#
from Configurables import Generation
Generation().EventType = 23103404
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phipipi0,KK=TightCut,FromD.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ => ^(phi(1020) => ^K+ ^K- ) ^(rho(770)+ => ^pi+ ^pi0)]CC'
tightCut.Cuts      =    {
    '[K+]cc'   : ' goodKaon ' , 
    '[pi+]cc'   : ' goodPion ' , 
    '[phi(1020)]cc'  : ' goodphi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPion = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodphi  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ] 


