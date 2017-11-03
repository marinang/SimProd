# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/20011001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 20011001
#
# ASCII decay Descriptor: pp => [<Xc>]cc ...
#
from Configurables import Generation
Generation().EventType = 20011001
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_c=MuonHighPTNoBForceC.dec"
Generation().Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/MuonCut"
Generation().Inclusive.InclusivePIDList = [ 421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441 ]
                                                                    
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "MuonCut" )
MuonCut = Generation().MuonCut                                                      
                                                                                        
MuonCut.Preambulo += [ 
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMuon     =  ( ('mu+' == GABSID ) & (GPT > 4 * GeV) & ( GTHETA < 400 * mrad ) )"
   , "Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors ) "
   , "notFromB     =  ( Bancestors == 0 )"
   , "Cancestors   =  GNINTREE ( GCHARM , HepMC.ancestors ) "
   , "fromC     =  ( Cancestors > 0 )"
   ]

MuonCut.Code = " ( count ( isGoodMuon & notFromB & fromC ) > 0 ) "                                          


