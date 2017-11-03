# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23513005.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 23513005
#
# ASCII decay Descriptor: [D_s+ -> ( tau+ -> p~- mu+ mu+ ) nu_tau ]cc
#
from Configurables import Generation
Generation().EventType = 23513005
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_taunu,pmm=SS,FromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ -> ( ^(tau+ -> ^p~- ^mu+ ^mu+) ) nu_tau ]CC'
tightCut.Cuts      =    {
    '[mu+]cc'  : ' goodMuon ' , 
    '[p~-]cc'  : ' goodProton ' , 
    '[tau+]cc' : ' goodTau  ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodProton = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodTau  = GHAS (GBEAUTY, HepMC.ancestors) ' ]


