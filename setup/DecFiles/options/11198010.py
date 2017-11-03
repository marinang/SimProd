# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11198010.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11198010
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (anti-D0 -> K+ pi+ pi- pi-) pi-) (D+ -> K- pi+ pi+ ) ]cc
#
from Configurables import Generation
Generation().EventType = 11198010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD,D0K3pi,Dkpipi=CPV,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ [B0]cc => ^( D*(2010)- => ^(D~0 -> ^K+ ^pi- ^pi+ ^pi-) ^pi-) ^(D+ => ^K- ^pi+ ^pi+)  ]CC'

tightCut.Preambulo += [
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'goodh        = (GPT > 100 * MeV)  & (GP > 1.0 *GeV) & inAcc',
   'goodD        = (GINTREE( (GPT > 450 * MeV ) & (GP > 4.5 * GeV ) ) ) ',
   'goodB        = (GINTREE( (GPT > 1500 * MeV ) & (GP > 9.5 * GeV ) ) ) & (GTIME > 0.05 * millimeter) & ( GCHILD( GPT , "D*(2010)-" == GABSID) + GCHILD(GPT ,"D+" == GABSID)  > 4.5 * GeV) '
   ]
tightCut.Cuts = {
  '[B0]cc'       : 'goodB' ,
  '[D~0]cc'      : 'goodD' ,
  '[D+]cc'       : 'goodD' ,
  '[K+]cc'       : 'goodh' ,
  '[pi+]cc'      : 'goodh'
  }

