# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574121.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15574121
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) mu+ nu_mu)  anti-nu_e e-]cc
#
from Configurables import Generation
Generation().EventType = 15574121
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcenu,L0munu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalPlain.HighVisMass
tightCut.Decay   = '[^(Lambda_b0 => ^(Lambda_c+ => ^(Lambda0 => ^p+ ^pi-) ^mu+ ^nu_mu) ^e- ^nu_e~)]CC'
tightCut.Cuts    =    {
    '[p+]cc'        : "inAcc",
    '[pi-]cc'       : "inAcc",
    '[mu+]cc'       : "inAcc",
    '[e-]cc'        : "inAcc",
    '[Lambda_b0]cc' : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'mu+' == GABSID , 'e-' == GABSID, 'p+' == GABSID, 'pi+' == GABSID ) ) > 4500 * MeV ) " ]

