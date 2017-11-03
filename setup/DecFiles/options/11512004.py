# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11512004.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11512004
#
# ASCII decay Descriptor: [B0 -> (K+ -> mu+ nu_mu) (pi- -> mu- nu_mu~)]CC
#
from Configurables import Generation
Generation().EventType = 11512004
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+pi-,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000 )
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ Beauty -> ^(K+ -> ^mu+ nu_mu) ^(pi- -> ^mu- nu_mu~ )]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, GeV" ,
    "decay = in_range ( -1 * meter,            GFAEVX ( GVZ, 100 * meter ),                    10 * meter ) ",
#   "decay = in_range ( -1 * meter , monitor ( GFAEVX ( GVZ, 100 * meter ) , '  decay-Z\n' ) , 10 * meter ) ",
    "inAcc = in_range ( 0.0075, GTHETA, 0.400 ) " , 
]
tightCut.Cuts      =    {
    '[K+]cc'   : ' decay & inAcc ',
    '[pi+]cc'  : ' decay & inAcc ',
#   '[mu+]cc'  : " 3 * GeV < monitor ( GP , '  mu P\n' )" , 
    '[mu+]cc'  : " 3 * GeV < GP " , 
                        }

