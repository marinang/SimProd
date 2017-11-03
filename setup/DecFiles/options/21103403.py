# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21103403.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 21103403
#
# ASCII decay Descriptor: [D+ -> (phi -> K+ K-) pi+ pi0]cc
#
from Configurables import Generation
Generation().EventType = 21103403
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D_phipipi0,KK=TightCut,FromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D+ => ( ^(phi(1020) => ^K+ ^K- ) ) ^pi+ ^pi0]CC'
tightCut.Cuts      =    {
    '[K+]cc'   : ' goodKaon ' , 
    '[pi+]cc'   : ' goodPion ' , 
    '[phi(1020)]cc'  : ' goodphi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPion = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodphi  = GHAS (GBEAUTY, HepMC.ancestors) ' ] 


