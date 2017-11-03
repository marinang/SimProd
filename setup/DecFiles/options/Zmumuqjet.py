# Pythia options for Z->mumujet 42112020
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )


# PYTHIA 6 OPTIONS
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.Commands += [ "pysubs msel 0" ,
                                                    "pysubs msub 30 1" ,


                                                    ### EXTRA OPTION TO SPEED UP
                                                    ### REMOVED TO MATCH PYTHIA8 PRODUCTION !
                                                    #"pysubs kfin 1 1 0",
                                                    #"pysubs kfin 1 2 0",
                                                    #"pysubs kfin 1 3 0", 
                                                    #"pysubs kfin 1 4 0",
                                                    #"pysubs kfin 1 5 1",
                                                    #"pysubs kfin 1 6 0",
                                                    #
                                                    #"pysubs kfin 1 -1 0",
                                                    #"pysubs kfin 1 -2 0",
                                                    #"pysubs kfin 1 -3 0", 
                                                    #"pysubs kfin 1 -4 0",
                                                    #"pysubs kfin 1 -5 1",
                                                    #"pysubs kfin 1 -6 0",
                                                    #
                                                    #"pysubs kfin 2 1 0",
                                                    #"pysubs kfin 2 2 0",
                                                    #"pysubs kfin 2 3 0", 
                                                    #"pysubs kfin 2 4 0",
                                                    #"pysubs kfin 2 5 1",
                                                    #"pysubs kfin 2 6 0",
                                                    #
                                                    #"pysubs kfin 2 -1 0",
                                                    #"pysubs kfin 2 -2 0",
                                                    #"pysubs kfin 2 -3 0", 
                                                    #"pysubs kfin 2 -4 0",
                                                    #"pysubs kfin 2 -5 1",
                                                    #"pysubs kfin 2 -6 0",
                                                    


                                                    "pypars mstp 43 2" ,
                                                    "pydat3 mdme 174 1 0" ,
                                                    "pydat3 mdme 175 1 0" ,
                                                    "pydat3 mdme 176 1 0" ,
                                                    "pydat3 mdme 177 1 0" ,
                                                    "pydat3 mdme 178 1 0" ,
                                                    "pydat3 mdme 179 1 0" ,
                                                    "pydat3 mdme 180 1 0" ,
                                                    "pydat3 mdme 181 1 0" ,
                                                    "pydat3 mdme 182 1 0" ,
                                                    "pydat3 mdme 183 1 0" ,
                                                    "pydat3 mdme 184 1 1" ,
                                                    "pydat3 mdme 185 1 0" ,
                                                    "pydat3 mdme 186 1 0" ,
                                                    "pydat3 mdme 187 1 0" ,
                                                    "pydat3 mdme 188 1 0" ,
                                                    "pydat3 mdme 189 1 0" ,
                                                    ]



## PYTHIA 8 OPTIONS
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
		"WeakZ0:gmZmode = 2",
		"WeakBosonAndParton:qg2gmZq = on",
		"23:onMode = off",
		"23:onIfAny = 13"
]
