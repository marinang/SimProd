# Main configuration file to generate Susy decay acc. to Kaplan's model
# Pile-Up, mk = 38 GeV, at least 1 k in accept.
# A file with options common to all models Kaplan.opts must be also included
# @author Neal Gauvin (Gueissaz) 
# @date 13 june 2008
#

from Configurables import Generation
from Gaudi.Configuration import *

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [
  #Set SUSY param
  "pymssm imss 1 1",  #Switch on SUSY  MSSM input from hand

  #Set Kaplan SUSY parameters imm 1 1
  "pymssm rmss 1 40",    #M1
  "pymssm rmss 2 1200",   #M2
  "pymssm rmss 4 1200",   #mu
  #"pymssm rmss 5 5.0",     #tanbeta
  "pymssm rmss 9 200",  #right sqark
  "pymssm rmss 10 200", #left sqark for third gener.
  "pymssm rmss 12 200" #right stop mass
  #"pymssm rmss 16 1000", #top trilinear coupling or common trilinear cplg A
]
