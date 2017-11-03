"""
@file

Main configuration file for long-lived RPV MSSM neutralino production

pp->( ~chi_10 -> (q anti-q' mu) ~chi_10 -> (q'' anti-q''' mu) )

Concrete dec files can specify a parameter point by setting the SLHA spectrum file

@code
#
# InsertPythonCode
# 
# Generation().Special.Pythia8Production.Commands.append("SLHA:file MyModelSpectrum.slha")
# 
# EndInserPythonCode
#
@endcode

@author Pieter David <pieter.david@cern.ch>
@date 2013-06-13
"""
__author__ = "Pieter David <pieter.david@cern.ch>"
__date__   = "2013-06-13"
# ============================================================================
from Configurables import Generation, Special, Pythia8Production

gen = Generation()
gen.addTool( Special )
gen.Special.addTool( Pythia8Production )
gen.Special.KeepOriginalProperties = True
prod = Generation().Special.Pythia8Production

gen.PileUpTool = "FixedLuminosityForRareProcess"

prod.Commands = [
      "SoftQCD:all = on"
    # turn on SUSY production
    , "SUSY:all = on"

    # be more verbose (useful for debugging)
    , "Main:timesAllowErrors = 0"
    , "SLHA:verbose = 3"
    , "Print:quiet = off"
    ]
#prod.OutputLevel = DEBUG
# ============================================================================
from Configurables import GaudiSequencer, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC

GenMonitor = GaudiSequencer( "GenMonitor" )
GenMonitor.Members += [
    GaussMonitor__CheckLifeTimeHepMC("HepMCLifeTime",
        Particles = [
            "~chi_10" ,
            "B0" , "B_s0" , "B+" , "B_c+" , "Lambda_b0" ,
            "D0" , "D+" , "D_s+" ,  "Lambda_c+"
        ]
    )
]
SimMonitor = GaudiSequencer( "SimMonitor" )
SimMonitor.Members += [
    GaussMonitor__CheckLifeTimeMC("MCLifeTime",
        Particles = [
            "~chi_10" ,
            "B0" , "B_s0" , "B+" , "B_c+" , "Lambda_b0" ,
            "D0" , "D+" , "D_s+" ,  "Lambda_c+"
        ]
    )
]
# ============================================================================
