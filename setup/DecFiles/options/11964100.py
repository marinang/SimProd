# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11964100.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11964100
#
# ASCII decay Descriptor: [[([B0]nos --> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ...)]CC, [([B0]os --> ^(D0  => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ...)]CC]
#
from Configurables import Generation
Generation().EventType = 11964100
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0X,KSKK=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[(Beauty&LongLived) --> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ... ]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter ',
    'inAcc     = in_range ( 0.01 , GTHETA , 0.350 ) ',
    'goodD0    = ( (GPT > 2000 * MeV) )',
    'kaoncuts  = ( GNINTREE( ("K+" == GABSID ) & (GP > 2000 * MeV) , 4) > 1.5 )',
    'pioncuts  = ( GNINTREE( ("pi+" == GABSID ) & (GP > 1800 * MeV) , 4) > 1.5 )',
    'trigger   = ( GNINTREE( (("pi+" == GABSID) | ("K+" == GABSID)) & (GPT > 1400 * MeV ) & (GP > 2700 * MeV) , 4)  > 0.5) ',
]
tightCut.Cuts      =    {
    '[pi+]cc'   : 'inAcc',
    '[K+]cc'    : 'inAcc',
    '[D0]cc'    : 'goodD0 & pioncuts & trigger & kaoncuts',
    }


