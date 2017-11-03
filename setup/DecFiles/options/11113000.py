# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11113000.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11113000
#
# ASCII decay Descriptor: [B0 -> (K*0 -> K+ pi-) (tau- -> TAUOLA) mu+]cc
#
from Configurables import Generation
Generation().EventType = 11113000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttaumu,3pipi0=DecProdCut,TightCut,tauola8,phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ B0 -> ^([mu+]CC) ([tau- ==> ^pi+ ^pi- ^pi- pi0 nu_tau]CC) ([K*(892)0 ==> ^K+ ^pi-]CC) ]CC'
tightCut.Cuts      =    {
    '[pi-]cc'   : ' goodPion  ' ,
    '[K+]cc'    : ' goodKaon  ' ,
    '[mu+]cc'   : ' goodMuon  ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import MeV',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'goodMuon  = ( GPT > 950  * MeV ) & inAcc' ,
    'goodKaon  = ( GPT > 220  * MeV ) & inAcc' ,
    'goodPion  = ( GPT > 220  * MeV ) & inAcc' ]


