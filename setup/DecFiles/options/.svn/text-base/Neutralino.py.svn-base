# @file
#  Options to include to produce neutralino. This contains pythia
#  commands to be set independently from the model to be used.
#  Must be included from model dependent options.
#
#  @author Neal Gauvin (Gueissaz)
#  @date   2008-10-23
#

#Cut Tool options
#Generation.Special.PythiaLSP.LSPCond = 1 ; //LSP in acceptance, Default
from Configurables import Generation, Special, PythiaLSP
Generation().addTool( Special )
Generation().Special.addTool( PythiaLSP ) 
Generation().Special.PythiaLSP.NbLSP = 1 
Generation().Special.PythiaLSP.AtLeast = True
Generation().Special.PythiaLSP.EtaMax = 1000.

from Configurables import PythiaProduction

Generation().Special.addTool( PythiaProduction )

# list of particles to be printed using PyList(12)
Generation().Special.PythiaProduction.PDTList = [ 1000022 ]

#Pile-up and luminosity
Generation().PileUpTool = "FixedLuminosityForRareProcess"

#set off unwanted processes
from Gaudi.Configuration import importOptions
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

