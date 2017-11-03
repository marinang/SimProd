# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574084.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11574084
#
# ASCII decay Descriptor: [B0 -> (D- -> (K*0 -> K+ pi-) e- anti-nu_e) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 11574084
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,Kstenu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalRepeatedHadronization.HighVisMass
tightCut.Decay   = '[^(B0 => ^(D- => ^(K*(892)0 => ^K+ ^pi-) ^e- ^nu_e~) ^mu+ ^nu_mu)]CC'
tightCut.Cuts    =    {
    '[K+]cc'     : "inAcc",
    '[pi-]cc'    : "inAcc",
    '[e-]cc'     : "inAcc",
    '[mu+]cc'     : "inAcc",
    '[B0]cc'     : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'e-' == GID , 'mu+' == GID, 'K+' == GABSID, 'pi+' == GABSID ) ) > 4500 * MeV ) " ]

