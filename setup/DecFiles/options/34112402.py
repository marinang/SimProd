# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34112402.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 34112402
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- pi0
#
from Configurables import Generation
Generation().EventType = 34112402
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 310 ]
                                                                          
#                                                                                          
from Configurables import LoKi__GenCutTool                                                 
gen = Generation()                                                                         
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )                                  
#                                                                                          
tightCut = gen.SignalPlain.TightCut                                                        
tightCut.Decay     = 'KS0 => mu+ mu- pi0'                                                      
tightCut.Preambulo += [                                                                    
    "GVX = LoKi.GenVertices.PositionX() " ,                                                
    "GVY = LoKi.GenVertices.PositionY() " ,                                                
    "GVZ = LoKi.GenVertices.PositionZ() " ,                                                
    "from GaudiKernel.SystemOfUnits import meter, millimeter, GeV" ,                       
    "vx      = GFAEVX ( GVX, 100 * meter ) " ,                                             
    "vy      = GFAEVX ( GVY, 100 * meter ) " ,                                             
    "rho2    = vx**2 + vy**2 " ,                                                           
    "rhoK  =  rho2 < (30 * millimeter )**2 " ,                                             
    "decay = in_range ( -1 * meter,  GFAEVX ( GVZ, 100 * meter ),    1 * meter ) ",                            
]                                                                                          
tightCut.Cuts      =    {                                                                  
    'KS0'  : ' decay & rhoK ',                                                             
                        }                                                                  

