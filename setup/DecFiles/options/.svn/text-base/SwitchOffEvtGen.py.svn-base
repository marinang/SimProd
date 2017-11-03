from Configurables import Generation, MinimumBias
from Configurables import Inclusive, SignalPlain, SignalRepeatedHadronization
from Configurables import Special, PythiaProduction


gen = Generation()
gen.DecayTool = ""
gen.addTool( MinimumBias , name = "MinimumBias" )
gen.MinimumBias.DecayTool = ""
gen.MinimumBias.KeepOriginalProperties = True

gen.addTool( Inclusive , name = "Inclusive" )
gen.Inclusive.DecayTool = ""
gen.Inclusive.KeepOriginalProperties = True

gen.addTool( SignalPlain , name = "SignalPlain" )
gen.SignalPlain.DecayTool = ""
gen.SignalPlain.KeepOriginalProperties = True

gen.addTool( SignalRepeatedHadronization , name = "SignalRepeatedHadronization" )
gen.SignalRepeatedHadronization.DecayTool = ""
gen.SignalRepeatedHadronization.KeepOriginalProperties = True

gen.addTool( Special , name = "Special" )
gen.Special.DecayTool = ""
gen.Special.KeepOriginalProperties = True

gen.MinimumBias.addTool( PythiaProduction , name = "PythiaProduction" ) 
gen.Inclusive.addTool( PythiaProduction , name = "PythiaProduction" ) 
gen.SignalPlain.addTool( PythiaProduction , name = "PythiaProduction" ) 
gen.SignalRepeatedHadronization.addTool( PythiaProduction ,
                                         name = "PythiaProduction" ) 
gen.Special.addTool( PythiaProduction , name = "PythiaProduction" ) 

gen.MinimumBias.PythiaProduction.Commands += [ "pysubs msub 485 0" ]
gen.Inclusive.PythiaProduction.Commands += [ "pysubs msub 485 0" ]
gen.SignalPlain.PythiaProduction.Commands += [ "pysubs msub 485 0" ]
gen.SignalRepeatedHadronization.PythiaProduction.Commands += [ "pysubs msub 485 0" ]
gen.Special.PythiaProduction.Commands += [ "pysubs msub 485 0" ]
