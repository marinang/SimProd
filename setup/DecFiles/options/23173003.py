# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23173003.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 23173003
#
# ASCII decay Descriptor: [D_s+ => ( phi(1020) => mu+ mu- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 23173003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phipi,mm=FromD.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ => ( ^(phi(1020) => ^mu+ ^mu-) ) ^pi+ ]CC'
tightCut.Cuts      =    {
    '[mu+]cc'   : ' goodMuon ' , 
    '[pi+]cc'   : ' goodPion ' , 
    '[phi(1020)]cc'  : ' goodPhi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPion = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPhi  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ] 


