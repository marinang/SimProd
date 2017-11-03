# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34102408.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 34102408
#
# ASCII decay Descriptor: K_S0 -> pi+ pi- pi0
#
from Configurables import Generation
Generation().EventType = 34102408
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_pippimpi0=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 310 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'KS0 => ^pi+ ^pi- pi0'
tightCut.Preambulo += [
    "from LoKiCore.functions import in_range"  ,
    "GVX = LoKi.GenVertices.PositionX() " ,
    "GVY = LoKi.GenVertices.PositionY() " ,
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,
    "vx      = GFAEVX ( GVX, 100 * meter ) " ,   
    "vy      = GFAEVX ( GVY, 100 * meter ) " ,
    "vz      = GFAEVX ( GVZ, 100 * meter ) " ,
    "rho2    = vx**2 + vy**2 " ,
    "rhoK  =  rho2 < (38 * millimeter )**2 " ,
    "decay =  vz <   (0.8 * meter ) ",
]
tightCut.Cuts      =    {
    'KS0'  : ' decay & rhoK ',
    '[pi+]cc'  : ' in_range( 0.010 , GTHETA , 0.400 ) ',
    '[pi-]cc'  : ' in_range( 0.010 , GTHETA , 0.400 ) '                                                                                                                                                         
                        }

