# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/30011000.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 30011000
#
# ASCII decay Descriptor: pp => ?
#
from Configurables import Generation
Generation().EventType = 30011000
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_MuonHighPTNoBNoC.dec"
Generation().MinimumBias.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/MuonCut"
                                                                    
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "MuonCut" )
MuonCut = Generation().MuonCut                                                      
                                                                                        
MuonCut.Preambulo += [                                                         
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMuon     =  ( ('mu+' == GABSID ) & (GPT > 4 * GeV) & ( GTHETA < 400 * mrad ) )"
   , "Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors ) "
   , "notFromB     =  ( Bancestors == 0 )"
   , "Cancestors   =  GNINTREE ( GCHARM , HepMC.ancestors ) "
   , "notFromC     =  ( Cancestors == 0 )"
   ]

MuonCut.Code = " ( count ( isGoodMuon & notFromB & notFromC ) > 0 ) "                                          


