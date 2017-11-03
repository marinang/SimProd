# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10011001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 10011001
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10011001
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=MuonHighPTForceB.dec"
Generation().Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/MuonCut"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]
                                                                    
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "MuonCut" )
MuonCut = Generation().MuonCut                                                      
                                                                                        
MuonCut.Preambulo += [           
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMuon     =  ( ('mu+' == GABSID ) & (GPT > 4 * GeV) & ( GTHETA < 400 * mrad ) )"
   , "Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors ) "
   , "fromB     =  ( Bancestors > 0 )"
   ]

MuonCut.Code = " ( count ( isGoodMuon & fromB ) > 0 ) "
                                         

