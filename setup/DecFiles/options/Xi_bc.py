from Configurables import ( Generation, Special, GenXiccProduction,
                            Pythia8Production )

gen = Generation()
gen.addTool( Special , name = "Special" )
gen.Special.addTool( GenXiccProduction , name = "GenXiccProduction" )

gen.Special.GenXiccProduction.Commands = [
  "mixevnt imix 1" ,
  "loggrade ivegasopen 0",
  "loggrade igrade 1",
  "vegasbin nvbin 300",  # grade files generated with these setting    
  "counter xmaxwgt 5000000",
  "confine pscutmin 1.9",
  "confine pscutmin 5.0"

]

gen.Special.GenXiccProduction.addTool( Pythia8Production )
gen.Special.GenXiccProduction.Pythia8Production.Commands += [
  'Check:epTolErr = 1'
]
