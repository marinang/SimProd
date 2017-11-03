# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/46000050.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 46000050
#
# ASCII decay Descriptor: pp -> ( (X -> ~chi_10 -> (l q q, l l l), X -> ~chi_1+ -> (l q q, l l l), X -> ~chi_1- -> (l q q, l l l)) + jet ... )
#
from Configurables import Generation
Generation().EventType = 46000050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/BRpVGaugino_m0800_m324000.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/AMSB_m0800_m324000.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/SusyBRpV.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHASpectrumFile = "AMSB_m0800_m324000.LHspc"
from Configurables import PythiaLSP
Generation().Special.addTool( PythiaLSP )
Generation().Special.PythiaLSP.LSPID = [ 1000022, 1000024 ]
