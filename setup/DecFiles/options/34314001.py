# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34314001.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 34314001
#
# ASCII decay Descriptor: (K_S0 -> mu+ mu- mu+ e-) (K_S0 -> mu+ mu- mu- e+)
#
from Configurables import Generation
Generation().EventType = 34314001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_3mue=TightCut,rho.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 310 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[KS0 -> mu+ mu- mu+ e-]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,
    "GVX = LoKi.GenVertices.PositionX() " ,
    "GVY = LoKi.GenVertices.PositionY() " ,
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "vx    = monitor( GFAEVX ( GVX, 100 * meter )  , ' vx-Ks\n')  " ,    
    "vy    = monitor( GFAEVX ( GVY, 100 * meter )  , ' vy-Ks\n')  " ,
    "rho2  = monitor(          vx**2 + vy**2       , ' rho2-Ks\n')" ,
    "rhoK  = monitor( rho2 < (30 * millimeter )**2 , ' rhoCut\n') " , 
    "decay = monitor( in_range ( -1 * meter, monitor( GFAEVX ( GVZ, 100 * meter ), ' SVZ-Ks\n'), 1 * meter ), ' SVZCut\n') ",
]
tightCut.Cuts      =    {
    'KS0'  : ' decay & rhoK',
                        }

