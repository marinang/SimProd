# Main configuration file to generate Susy decay acc. to Kaplan's model
# Pile-Up, mk = 98 GeV, at least 1 k in accept
# @author Neal Gauvin (Gueissaz) 
# @date 9 october 2008
#

#Provide a decay file to pythia
#Generation.Special.PythiaProduction.SLHADecayFile = "Kaplan_mk98.dec";

from Configurables import Generation, Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.PDecayList = [ 1000022 ]

Generation().Special.PythiaProduction.Commands += [

  #Set SUSY param
  "pymssm imss 1 1",  #Switch on SUSY  MSSM input from hand

  #Set Kaplan SUSY parameters imm 1 1
  "pymssm rmss 1 100",    #M1
  "pymssm rmss 2 1200",   #M2
  "pymssm rmss 4 1200",   #mu
  #"pymssm rmss 5 5.0",     #tanbeta
  "pymssm rmss 9 200",  #right sqark
  "pymssm rmss 10 200", #left sqark for third gener.
  "pymssm rmss 12 200"  #right stop mass
  #"pymssm rmss 16 1000", #top trilinear coupling or common trilinear cplg A
]
