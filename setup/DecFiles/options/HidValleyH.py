from Gaudi.Configuration import *
from Configurables import *
# ============================================================================
"""
@file

The main configuration file to run the production of
various variants of "Hidden Valley through Higgses" :

    pp->(  H_20 -> ( H_30 -> q anti-q ) ( H_30 -> q' anti-q') )

Each concrete dec file needs to specify the properties of
H_20 and H_30 separately, e.g.:

@code
#
# InsertPythonCode:
#
# ### include this "common" configuration file:
#
# from Gaudi.Configuration import *
# importOptions( "$DECFILESROOT/options/HidValleyH.py" )
#
# ### specify the Higgs and HV-pion decay modes
#
# Generation().Special.PythiaProduction.Commands[:0] = [
#     "pyinit pdtinput $DECFILESROOT/ppfiles/HiddenValleyHiggses_bbbar.pdt"
# ]
#
# EndInsertPythonCode
#
# ### define the particular properties of H_20 and H_30
#
# ParticleValue: "H_20 88 35 0.0 120.0 9.4e-26 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0  35.0 1.0e-11      A0 36 0.0e+00"
#
@endcode

===========================================
"Hidden Valley through Higgses"
===========================================
event type   m(H0)  m(A0)    t(A0)  flavour
===========================================
43900004     120     15      10ps         b
43900005     120     50      10ps         b
43900006     120     35      10ps         c
43900007     120     35      10ps     u/d/s
43900011     120     35       1ps         b
43900012     120     35      10ps         b
43900013     120     35     100ps         b
43900014     120     35      10ps        mu
43900015     120     43      10ps         b
43900016     120     15     100ps         b
25900017     120     25     100ps         b
43900018     120     43     100ps         b
43900019     120     50     100ps         b
43900020     120     25      10ps         b
===========================================

@author Vanya BELYAEV ibelyaev@physics.syr.edu
@date 2006-10-20

@author Pieter David pieter.david@cern.ch
@date 2011-02-07
@date 2014-06-02
"""

# ==============================================================================
# Pythia6 settings
# ==============================================================================

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands = [
    "pyinit pdtlevel 3"
]

Generation().Special.PythiaProduction.PygiveCommands = [
    # regular minimum bias events
    "MSEL=0"      ,
    # store the documentation strings ?
    "MSTP(128)=2" ,   # VERY IMPORTANT to preserve the event history!
    # Switch ON processes for H0(H_20) Production:
    # 151 f + fbar -> H0
    # 152 g + g -> H0
    "MSUB(151)=1","MSUB(152)=1","MSUB(153)=1" ,
    # 171 f + fbar -> Z0 + H0
    # 172 f + fbar' -> W+/- + H0
    # 173 f + f' -> f + f' + H0
    # 174 f + f' -> f" + f"' + H0
    "MSUB(171)=1","MSUB(172)=1","MSUB(173)=1","MSUB(174)=1" ,
    # 181 g + g -> Q + Qbar + H0
    # 182 q + qbar -> Q + Qbar + H0
    # 183 q + qbar -> g + H0
    # 184 q + g -> q + H0
    # 185 g + g -> g + H0
    "MSUB(181)=1","MSUB(182)=1","MSUB(183)=1","MSUB(184)=1" ,
    # 185 g + g -> g + H0
    "MSUB(185)=1" ,
    # Switch OFF processes :
    # 11 f + f' -> f + f' (QCD)
    # 12 f + fbar -> f' + fbar'
    # 13 f + fbar -> g + g
    "MSUB(11)=0","MSUB(12)=0","MSUB(13)=0"  ,
    # 28 f + g -> f + g
    # 53 g + g -> f + fbar
    # 68 g + g -> g + g
    "MSUB(28)=0","MSUB(53)=0","MSUB(68)=0"  ,
    # 71 Z0 + Z0 -> Z0 + Z0
    # 72 Z0 + Z0 -> W+ + W-
    # 73 Z0 + W+/- -> Z0 + W+/-
    # 76 W+ + W- -> Z0 + Z0
    # 77 W+/- + W+/- -> W+/- + W+/-
    "MSUB(71)=0","MSUB(72)=0","MSUB(73)=0","MSUB(76)=0","MSUB(77)=0" ,
    # 86 g + g -> J/Psi + g
    # 87 g + g -> chi_0c + g
    # 88 g + g -> chi_1c + g
    # 89 g + g -> chi_2c + g
    "MSUB(86)=0","MSUB(87)=0","MSUB(88)=0","MSUB(89)=0"  ,
    # 91 Elastic scattering
    # 92 Single diffractive (XB)
    # 93 Single diffractive (AX)
    # 93 Single diffractive (AX)
    # 95 Low-pT scattering
    "MSUB(91)=0","MSUB(92)=0","MSUB(93)=0","MSUB(94)=0","MSUB(95)=0" ,
    # 106 g + g -> J/Psi + gamma
    "MSUB(106)=0"
]
Generation().Special.PythiaProduction.UpdatedParticles = [ 35, 36 ] # H0 and V0-pion specified in the dec file

Generation().Special.PythiaProduction.ValidateHEPEVT = True

# ==============================================================================
# Pythia6 settings
# ==============================================================================
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
      "SpaceShower:rapidityOrder = off" #pT ordering!
    , "PartonLevel:FSR=on"              # FSR by PYTHIA8 (NOT PHOTOS)
    , "Higgs:useBSM      = on"
    , "HiggsBSM:gg2H2    = on" # produce gg->H^0(H2)
    # SM couplings (total width and production)
    , "HiggsH2:coup2H1H1 = 0."
    , "HiggsH2:coup2A3A3 = 0."
    , "35:addChannel     = on 1.e-2 101 36 36" # me: partial width from total width and BR
    , "35:onMode         = off"
    , "35:onIfAll        = 36 36"
    , "35:doForceWidth   = on"
] 
Generation().Special.Pythia8Production.ValidateHEPEVT = False
# ============================================================================
GenerationToSimulation("GenToSim").KeepCode = "in_list( GABSID, [ 'H_20', 'H_30' ] ) & ( GSTATUS == LHCb.HepMCEvent.DocumentationParticle )"

# ============================================================================
GenMonitor = GaudiSequencer( "GenMonitor" )
GenMonitor.Members += [
    GaussMonitor__CheckLifeTimeHepMC("HepMCLifeTime",
        Particles = [
            "H_20" , "H_30" ,
            "B0" , "B_s0" , "B+" , "B_c+" , "Lambda_b0" ,
            "D0" , "D+" , "D_s+" ,  "Lambda_c+"
        ]
    )
]
SimMonitor = GaudiSequencer( "SimMonitor" )
SimMonitor.Members += [
    GaussMonitor__CheckLifeTimeMC("MCLifeTime",
        Particles = [
            "H_20" , "H_30" ,
            "B0" , "B_s0" , "B+" , "B_c+" , "Lambda_b0" ,
            "D0" , "D+" , "D_s+" ,  "Lambda_c+"
        ]
    )
]
# ============================================================================
gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_20", "H_30"]
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]
#set off unwanted processes
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )
# ============================================================================
Generation().PileUpTool = "FixedLuminosityForRareProcess"
