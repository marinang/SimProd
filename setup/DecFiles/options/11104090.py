# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104090.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11104090
#
# ASCII decay Descriptor: [B0 -> K+ pi- pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11104090
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kpipipi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay   = "[^(B0 -> ^K+ ^pi- ^pi+ ^pi-)]CC"
tightCut.Preambulo += [
    "CS    = LoKi.GenChild.Selector",
    'inAcc = in_range ( 0.010 , GTHETA , 0.400 )' ,
    'm12 = GMASS(CS(1),CS(2))',
    'm34 = GMASS(CS(3),CS(4))',
    'm14 = GMASS(CS(1),CS(4))',
    'm23 = GMASS(CS(2),CS(3))']
tightCut.Cuts    =    {
    '[K+]cc'    : "inAcc",
    '[pi-]cc'   : "inAcc",
    '[B0]cc'    : "( ( (  m12  < 1.25 * GeV ) & ( m34 < 1.25 * GeV ) ) | ( ( m14 < 1.25 * GeV ) & ( m23 < 1.25 * GeV ) ) )" }


