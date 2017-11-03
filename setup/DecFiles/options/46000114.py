# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/46000114.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 46000114
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> mu q q' )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/RPVMSSMNeutralinoPythia8.py" )
from Configurables import Generation
Generation().EventType = 46000114
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/BRpVNeutralino_m0200_m12200_muqq_mSUGRA.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Chi10InAccMuInAcc"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/SusyBRpV.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHASpectrumFile = "mSUGRA_m0200_m12200_muqq.LHspc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "Chi10InAccMuInAcc" )
GenLevelSelection = Generation().Chi10InAccMuInAcc
GenLevelSelection.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad, mm, meter"
    , "GEVZ                   =  GFAEVX( GVZ, LoKi.Constants.InvalidDistance )"
    , "GEVRHO                 =  GFAEVX( GVRHO, LoKi.Constants.HugeDistance )"
    , "inAcceptance           = ( GTHETA < 400.*mrad ) & ( GP > 2.0*GeV )"
    , "decInVeloAcceptance    = in_range( -250.*mm, GEVZ, 750.*mm ) & ( GEVRHO < 82.*mm )"
    , "isNeutralino           = ( '~chi_10' == GABSID )"
    , "isGoodMu               = ( ( 'mu+' == GABSID ) & inAcceptance )"
    , "isGoodNeutralinoWithMu = ( isNeutralino & inAcceptance & decInVeloAcceptance & ( GNINTREE( isNeutralino, HepMC.descendants ) == 0 ) & ( GNINTREE( isGoodMu, HepMC.descendants ) > 0 ) )"
    ]
GenLevelSelection.Code = " count ( isGoodNeutralinoWithMu ) > 0 "

from Configurables import GenerationToSimulation
GenerationToSimulation("GenToSim").KeepCode = "( '~chi_10' == GABSID )" # Keep MCParticles Neutralinos

### Particle properties
spcFileName = "$DECFILESROOT/lhafiles/mSUGRA_m0200_m12200_muqq.LHspc"
specialSusyParticles = [ "1000022" ]

import sys,os
sys.path.append(os.path.expandvars("$DECFILESROOT/scripts/"))
from SuSySLHAFunctions import getParticlePropertiesAndPythia8Commands
pps, ppCommands = getParticlePropertiesAndPythia8Commands(spcFileName, specialSusyParticles)

Generation().Special.Pythia8Production.Commands += [
      "SLHA:file            %s" % spcFileName
    , "SLHA:useDecayTable = true"
    ] + ppCommands

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles += [
      "~chi_10 884  1000022  0.0 %e %e unknown  1000022 0.00000000" % pps["1000022"]
    ]

