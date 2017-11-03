# @file
#  Options to include to produce Z->bbbar.
#
#  @author Neal Gauvin (Gueissaz)
#  @date   3 august 2009
#

#Pile-up and luminosity
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.PDTList = [ 23, 24 ]

Generation().Special.PythiaProduction.Commands += [ 
    #"pyinit pyliste 3"
    
    "pysubs msel 0" ,
    "pysubs msub 1 1" ,
    "pysubs msub 2 0" ,
    "pysubs msub 15 1" ,
    "pysubs msub 16 0" ,
    "pysubs msub 19 1" ,
    "pysubs msub 20 0" ,
    "pysubs msub 22 1" ,
    "pysubs msub 23 1" , #Fi fjbar->Z+W
    "pysubs msub 25 0" ,
    "pysubs msub 30 1" ,
    "pysubs msub 31 0" ,
    
    #Only Z production
    "pypars mstp 43 2" ,
    
    #Z->bbbar
    "pydat3 mdme 174 1 0" ,
    "pydat3 mdme 175 1 0" ,
    "pydat3 mdme 176 1 0" ,
    "pydat3 mdme 177 1 0" ,
    "pydat3 mdme 178 1 1" ,
    "pydat3 mdme 179 1 0" ,
    "pydat3 mdme 180 1 0" ,
    "pydat3 mdme 181 1 0" ,
    "pydat3 mdme 182 1 0" ,
    "pydat3 mdme 183 1 0" ,
    "pydat3 mdme 184 1 0" ,
    "pydat3 mdme 185 1 0" ,
    "pydat3 mdme 186 1 0" ,
    "pydat3 mdme 187 1 0" ,
    "pydat3 mdme 188 1 0" ,
    "pydat3 mdme 189 1 0"  
    
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

#Cut Tool options : >= 4 b in acceptance
#Generation.ParticlesInAcceptance.PartCond = 1 ;
#Generation.ParticlesInAcceptance.NbPart = 4 ;
#Generation.ParticlesInAcceptance.AtLeast = true ;
#Generation.ParticlesInAcceptance.EtaMax = 1000.;
#Generation.ParticlesInAcceptance.PartID = { 3,4,5 } ;

#Cut Tool options
from Configurables import PythiaLSP

Generation().Special.CutTool = PythiaLSP
Generation().Special.addTool( PythiaLSP )
Generation().Special.PythiaLSP.LSPID = [ 5 ]
Generation().Special.PythiaLSP.LSPCond = 1 #following daughters in acc
Generation().Special.PythiaLSP.NbLSP = 4 
Generation().Special.PythiaLSP.EtaMax = 1000.
Generation().Special.PythiaLSP.OutputLevel = 3


#set off unwanted processes
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )
