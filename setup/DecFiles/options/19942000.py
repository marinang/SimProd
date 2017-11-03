# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/19942000.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 19942000
#
# ASCII decay Descriptor: pp =>  ( Xb --> J/psi(1S) ... )  ( Xb --> J/psi(1S) ... )
#
from Configurables import Generation
Generation().EventType = 19942000
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=2xJpsi.dec"
Generation().RepeatDecay.Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Cut2xJpsi"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "Cut2xJpsi" )
eventCut = Generation().Cut2xJpsi
eventCut.Code = " 1 < count ( jpsi )"
eventCut.Preambulo += [
 "fromB  = 0 != GNINTREE ( GBEAUTY , HepMC.ancestors ) " , 
 "jpsi   = ( 'J/psi(1S)' == GID ) & in_range ( 2 , GY , 4.5 ) & fromB "
 ]

