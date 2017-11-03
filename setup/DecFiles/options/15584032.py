# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15584032.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15584032
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- e+ nu_e) e- anti-nu_e p+]cc
#
from Configurables import Generation
Generation().EventType = 15584032
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0penu,Kenu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalPlain.HighVisMass
tightCut.Decay = "[^(Lambda_b0 => (D0 => ^K- ^e+ nu_e) ^e- nu_e~ ^p+)]CC"
tightCut.Cuts    =    {
    '[K-]cc'      : "inAcc",
    '[p+]cc'      : "inAcc",
    '[e+]cc'      : "inAcc",
    '[e-]cc'      : "inAcc",
    '[Lambda_b0]cc'     : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'e+' == GID , 'e-' == GID, 'K-' == GABSID, 'p+' == GABSID ) ) > 4500 * MeV ) " ]

