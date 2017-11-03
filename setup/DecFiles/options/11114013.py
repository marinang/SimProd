# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114013.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11114013
#
# ASCII decay Descriptor: [B0 => mu+ mu- K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11114013
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kpimumu,phsp=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay   = "[^(Beauty => ^mu+ ^mu- ^K+ ^pi-)]CC"
tightCut.Cuts    =    {
    '[B0]cc'    : " goodB & inPsqWin",
    '[K+]cc'    : " goodTrack " ,
    '[pi-]cc'   : " goodTrack " ,
    'mu-'       : " goodMuon  " ,
    'mu+'       : " goodMuon  " }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    "inPsqWin  = ( ( GMASS ( 'K+' == GABSID , 'pi-' == GABSID ) ) < 2000 * MeV ) " ,
    'goodB     = ( GPT > 1500 * MeV )                ' ,
    'goodTrack = ( GP  > 800 * MeV ) & inAcc ' ,
    'goodMuon  = ( GP  > 2000 * MeV ) & inAcc ' ]

