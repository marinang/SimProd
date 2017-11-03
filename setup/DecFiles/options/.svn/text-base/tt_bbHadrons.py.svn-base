# Generation of top quarks with decay into b W, W decays into hadrons.
# @author Neal Gauvin (Gueissaz) 
# @date 3 august 2009
#
from Configurables import Generation
from Gaudi.Configuration import *

#Top quark generation
importOptions( "$DECFILESROOT/options/Top.py" )


# list of particles to be printed using PyList(12)
from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.PDTList = [ 6, 24 ]

Generation().Special.PythiaProduction.Commands += [
    #W->Hadrons
   "pydat3 mdme 190 1 1" ,
   "pydat3 mdme 191 1 1" ,
   "pydat3 mdme 192 1 1" ,
   "pydat3 mdme 193 1 0" ,
   "pydat3 mdme 194 1 1" ,
   "pydat3 mdme 195 1 1" ,
   "pydat3 mdme 196 1 1" ,
   "pydat3 mdme 197 1 0" ,
   "pydat3 mdme 198 1 1" ,
   "pydat3 mdme 199 1 1" ,
   "pydat3 mdme 200 1 1" ,
   "pydat3 mdme 201 1 0" ,
   "pydat3 mdme 202 1 0" ,
   "pydat3 mdme 203 1 0" ,
   "pydat3 mdme 204 1 0" ,
   "pydat3 mdme 205 1 0",
   "pydat3 mdme 206 1 0", #enu
   "pydat3 mdme 207 1 0", #munu
   "pydat3 mdme 208 1 0",
   "pydat3 mdme 209 1 0"
]

#Cut Tool options
Generation().Special.CutTool = "PythiaLSP"
from Configurables import PythiaLSP
Generation().Special.addTool( PythiaLSP )
Generation().Special.PythiaLSP.LSPID = [ 6 ]
Generation().Special.PythiaLSP.LSPCond = 2 # following daughters in acc
Generation().Special.PythiaLSP.DgtsInAcc = [ 3,4,5,23,24 ]
Generation().Special.PythiaLSP.NbLSP = 2 
Generation().Special.PythiaLSP.EtaMax = 1000.
Generation().Special.PythiaLSP.OutputLevel = 3
