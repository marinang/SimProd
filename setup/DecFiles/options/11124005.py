# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11124005.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11124005
#
# ASCII decay Descriptor: {[[B0]nos -> e+ e- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> e- e+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11124005
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstee,phsp=DecProdCut,TightCut150MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay   = '[^(B0 => ^(K*(892)0 => ^K+ ^pi- ) ^e+ ^e- )]CC'
tightCut.Cuts    =    {
    '[K+]cc'	   : "inAcc",
    '[pi-]cc'    : "inAcc",
    '[e+]cc'     : "inAcc",
    '[e-]cc'     : "inAcc", 
    '[B0]cc'     : "lowMee" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "lowMee  = ( ( GMASS ( 'e+' == GID , 'e-' == GID ) ) < 150 * MeV ) " ]

