from Configurables import Generation, Special, BcVegPyProduction

BcVegPyListOfCommands = [
    "mixevnt imix 0" ,       # Turn off mixing of states.
    "counter ibcstate 1",    # Enable B_c[1S0] production.
    "loggrade igenerate 1",  # Generate full event.
    "loggrade ivegasopen 0", # Do not use VEGAS integration.
    "loggrade igrade 1"      # Use the existing gradient.
    ]

gen = Generation()
gen.addTool( Special , name = "Special" )
gen.Special.ProductionTool = "BcVegPyProduction"
gen.Special.addTool( BcVegPyProduction , name = "BcVegPyProduction" )
gen.Special.BcVegPyProduction.Commands += BcVegPyListOfCommands
gen.PileUpTool = "FixedLuminosityForRareProcess"
