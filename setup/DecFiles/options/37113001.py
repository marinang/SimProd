# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/37113001.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 37113001
#
# ASCII decay Descriptor: [ K+ -> pi+ mu- mu+ ]cc
#
from Configurables import Generation
Generation().EventType = 37113001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+_pi+mu-mu+=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 321,-321 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[^(K+ => ^pi+ ^mu- ^mu+)]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,
    "inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         " ,
    "inEta        =  in_range ( 1.95  , GETA   , 5.050 )         " ,
    "fastTrack    =  ( GP  > 1.5 * GeV )   & ( GPT > 50 * MeV )" ,
    "goodTrack    =  inEta & fastTrack & inAcc                   " ,     
    "GVX = LoKi.GenVertices.PositionX()                          " ,
    "GVY = LoKi.GenVertices.PositionY()                          " ,
    "GVZ = LoKi.GenVertices.PositionZ()                          " ,
    "vx      = GFAEVX ( GVX, 100 * meter )                       " ,    
    "vy      = GFAEVX ( GVY, 100 * meter )                       " ,
    "rho2    = vx**2 + vy**2                                     " ,
    "rhoK  =  rho2 < ( 1000 * millimeter )**2                      " , 
    "decay = in_range ( -0.1 * meter,  GFAEVX ( GVZ, 100 * meter ),  2.27 * meter ) ",
    "positivez = ( GPZ > 0 * MeV )                                         ",
    "kpt  = ( GPT > 90 *MeV )                                          ",
]
tightCut.Cuts      =    {
    '[K+]cc'  : ' decay & rhoK & positivez & kpt ',
    '[pi+]cc' : ' goodTrack ',
    '[mu+]cc' : ' goodTrack '
                        }

