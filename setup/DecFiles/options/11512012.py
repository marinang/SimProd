# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11512012.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11512012
#
# ASCII decay Descriptor: [B0 => pi- nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 11512012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pimunu=DecProdCut,M4.5GeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalRepeatedHadronization.TightCut
#
tightCut.Decay    = "[B0 => pi- mu+ nu_mu]CC"
tightCut.Cuts     = {
   '[B0]cc'  : "GINTREE((GABSID == 'pi+') & (ACC)) & GINTREE((GABSID == 'mu+') & (ACC)) & (BM2 > 20250000.)",
   }
#
tightCut.Preambulo += [
   "BPX2 = (GCHILD(GPX,'pi+' == GABSID) + GCHILD(GPX,'mu+' == GABSID))**2",
   "BPY2 = (GCHILD(GPY,'pi+' == GABSID) + GCHILD(GPY,'mu+' == GABSID))**2",
   "BPZ2 = (GCHILD(GPZ,'pi+' == GABSID) + GCHILD(GPZ,'mu+' == GABSID))**2",
   "BPE2 = (GCHILD(GE ,'pi+' == GABSID) + GCHILD(GE, 'mu+' == GABSID))**2",
   "BM2  = (BPE2 - BPX2 - BPY2 - BPZ2)" ,
   "ACC  = in_range ( 0.0075, GTHETA, 0.400 )" , 
   ]

