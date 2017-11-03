# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23513013.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 23513013
#
# ASCII decay Descriptor: [D_s+ -> mu+ (phi -> K+ K-) nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23513013
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phimunu,KK=TightCut,FromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[D_s+ => ^(phi(1020) => ^K+ ^K- ) ^mu+ ^nu_mu]CC'
tightCut.Cuts      =    {
    '[K+]cc'   : ' goodKaon ' , 
    '[mu+]cc'   : ' goodMuon ' , 
    '[phi(1020)]cc'  : ' goodphi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodphi  = GHAS (GBEAUTY, HepMC.ancestors) ' ] 


