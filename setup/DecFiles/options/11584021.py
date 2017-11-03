# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11584021.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11584021
#
# ASCII decay Descriptor: [B0 -> (D- -> (K*0 -> K+ pi-) e- anti-nu_e) e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 11584021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Denu,Kstenu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalRepeatedHadronization.HighVisMass
tightCut.Decay   = '[^(B0 => ^(D- => ^(K*(892)0 => ^K+ ^pi-) ^e- ^nu_e~) ^e+ ^nu_e)]CC'
tightCut.Cuts    =    {
    '[K+]cc'     : "inAcc",
    '[pi-]cc'    : "inAcc",
    '[e+]cc'     : "inAcc",
    '[e-]cc'     : "inAcc",
    '[B0]cc'     : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'e+' == GID , 'e-' == GID, 'K+' == GABSID, 'pi+' == GABSID ) ) > 4500 * MeV ) " ]

