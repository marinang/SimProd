# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574101.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 15574101
#
# ASCII decay Descriptor: {[ Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) pi+)  anti-nu_mu mu-]cc}
#
from Configurables import Generation
Generation().EventType = 15574101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,L0Pi=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalPlain.HighVisMass
tightCut.Decay   = '[^(Lambda_b0 => ^(Lambda_c+ => ^(Lambda0 => ^p+ ^pi-) ^pi+) ^mu- ^nu_mu~)]CC'
tightCut.Cuts    =    {
    '[p+]cc'        : "inAcc",
    '[pi-]cc'       : "inAcc",
    '[pi+]cc'       : "inAcc",
    '[mu-]cc'        : "inAcc",
    '[Lambda_b0]cc' : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'pi+' == GABSID , 'mu-' == GABSID, 'p+' == GABSID, 'pi+' == GABSID ) ) > 4500 * MeV ) " ]

