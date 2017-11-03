# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104004.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11104004
#
# ASCII decay Descriptor: [B0 -> K+ K- pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11104004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KpiKpi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay   = "[^(B0 => ^K+ ^K- ^pi+ ^pi-)]CC"
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.010 , GTHETA , 0.400 )' ,
    "lowMKpi   = ( ( GMASS ( 'K+' == GID , 'pi-' == GID ) ) < 2000 * MeV ) & ( ( GMASS ( 'K-' == GID , 'pi+' == GID ) ) < 2000 * MeV )" ]
tightCut.Cuts    =    {
    '[K+]cc'    : "inAcc",
    '[pi-]cc'   : "inAcc",
    '[B0]cc'  : "lowMKpi" }


