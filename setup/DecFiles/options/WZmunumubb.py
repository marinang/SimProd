# Pythia options for WZ->mumu,bb 42911000
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [ "pysubs msel 0" , 
                                                    "pysubs msub 23 1" ,
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
                                                    "pydat3 mdme 189 1 0" ,
                                                    "pydat3 mdme 190 1 0" ,
                                                    "pydat3 mdme 191 1 0" ,
                                                    "pydat3 mdme 192 1 0" ,
                                                    "pydat3 mdme 193 1 0" ,
                                                    "pydat3 mdme 194 1 0" ,
                                                    "pydat3 mdme 195 1 0" ,
                                                    "pydat3 mdme 196 1 0" ,
                                                    "pydat3 mdme 197 1 0" ,
                                                    "pydat3 mdme 198 1 0" ,
                                                    "pydat3 mdme 199 1 0" ,
                                                    "pydat3 mdme 200 1 0" ,
                                                    "pydat3 mdme 201 1 0" ,
                                                    "pydat3 mdme 202 1 0" ,
                                                    "pydat3 mdme 203 1 0" ,
                                                    "pydat3 mdme 204 1 0" ,
                                                    "pydat3 mdme 205 1 0" ,
                                                    "pydat3 mdme 206 1 0" ,
                                                    "pydat3 mdme 207 1 1" ,
                                                    "pydat3 mdme 208 1 0" ,
                                                    "pydat3 mdme 209 1 0"
                                                    ]
