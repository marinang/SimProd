# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104022.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11104022
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) (K*(892)0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_phiKst0=DecProdCut,Tightcut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
gen = Generation() 
gen.SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay =   '[^(B0 ==> ^(phi(1020) -> ^K+ ^K-) ^(K*(892)0 => ^K+ ^pi-))]CC'

tightCut.Cuts      =    {
   '[B0]cc'           : 'goodB' ,
   '[K*(892)0]cc'     : 'goodKst ',
   '[phi(1020)]cc'    : 'goodPhi ',
   '[K+]cc'           : 'goodTrack ' ,
   '[pi+]cc'          : 'goodTrack ' }
tightCut.Preambulo += [
   'from GaudiKernel.SystemOfUnits import ns, GeV, MeV, mrad',
   'inAcc      = in_range ( 0.01 , GTHETA , 0.400 ) ' ,
   'goodB      = ( GP > 5 *GeV ) & (GPT > 500 *MeV) & (GTIME > 0. *ns) ' ,
   'goodKst    = ( GPT > 500  *MeV )  ' ,
   'goodPhi    = ( GPT > 500  *MeV )  ' ,
   'goodTrack  = ( GPT > 250  *MeV )  & inAcc ' ]


