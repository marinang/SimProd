# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40911006.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 40911006
#
# ASCII decay Descriptor: pp -> {[W+ -> {mu+ nu_mu, e+ nu_e}]cc, (Z0 -> {mu+ mu-, e+ e-})} (H_10 -> b anti-b)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Higgs.py" )
from Configurables import Generation
Generation().EventType = 40911006
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_bb=mH120GeV,onlyl,10GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 0
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 120.000 9.400e-026 Higgs0 25 0.000e+000" ]
