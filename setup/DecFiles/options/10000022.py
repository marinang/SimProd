# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10000022.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 10000022
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10000022
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=Biased_LifetimeAll5ps.dec"
Generation().Inclusive.CutTool = "BiasedBB"
from Configurables import BiasedBB
Generation().Inclusive.addTool( BiasedBB )
Generation().Inclusive.BiasedBB.RadiusMin = 0.4
Generation().Inclusive.BiasedBB.NumberOfBMin = 1
Generation().Inclusive.BiasedBB.EtaMax = 5.0
Generation().Inclusive.BiasedBB.EtaMin = 1.5
Generation().Inclusive.BiasedBB.PtMin = 2.
Generation().Inclusive.BiasedBB.VMin = 0.0
Generation().Inclusive.BiasedBB.CTauMin = 0
Generation().Inclusive.BiasedBB.MinBDeltaPhi = 0
Generation().Inclusive.BiasedBB.MinChargedDaug = 1
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [
###                  GEANTID       PDGID  CHARGE      MASS(GeV)        TLIFE(s)               EVTGENNAME    PYTHIAID        MAXWIDTH
    "B0                   73         511  0.0        5.27953000   5.000000e-012                       B0         511   0.000000e+000"
  , "B~0                  74        -511  0.0        5.27953000   5.000000e-012                  anti-B0        -511   0.000000e+000"
  , "B0H               99998         510  0.0        5.27953000   5.000000e-012                      B0H           0   0.000000e+000"
  , "B0L               99999         150  0.0        5.27953000   5.000000e-012                      B0L           0   0.000000e+000"
  , "B+                   71         521  1.0        5.27915000   5.000000e-012                       B+         521   0.000000e+000"
  , "B-                   72        -521 -1.0        5.27915000   5.000000e-012                       B-        -521   0.000000e+000"
  , "B_s0                 75         531  0.0        5.36630000   5.000000e-012                     B_s0         531   0.000000e+000"
  , "B_s~0                76        -531  0.0        5.36630000   5.000000e-012                anti-B_s0        -531   0.000000e+000"
  , "B_s0H             99996         530  0.0        5.36630000   5.000000e-012                    B_s0H           0   0.000000e+000"
  , "B_s0L             99997         350  0.0        5.36630000   5.000000e-012                    B_s0L           0   0.000000e+000"
  , "B_c+                 77         541  1.0        6.27600000   5.000000e-012                     B_c+         541   0.000000e+000"
  , "B_c-                 78        -541 -1.0        6.27600000   5.000000e-012                     B_c-        -541   0.000000e+000"
  , "Lambda_b0            79        5122  0.0        5.62020000   5.000000e-012                Lambda_b0        5122   0.000000e+000"
  , "Lambda_b~0           80       -5122  0.0        5.62020000   5.000000e-012           anti-Lambda_b0       -5122   0.000000e+000"
  , "Xi_b-               122        5132 -1.0        5.79240000   5.000000e-012                    Xi_b-        5132   0.000000e+000"
  , "Xi_b~+              123       -5132  1.0        5.79240000   5.000000e-012               anti-Xi_b+       -5132   0.000000e+000"
  , "Xi_b0               124        5232  0.0        5.79240000   5.000000e-012                    Xi_b0        5232   0.000000e+000"
  , "Xi_b~0              125       -5232  0.0        5.79240000   5.000000e-012               anti-Xi_b0       -5232   0.000000e+000"
  , "Omega_b-            120        5332 -1.0        6.12000000   5.000000e-012                 Omega_b-        5332   0.000000e+000"
  , "Omega_b~+           121       -5332  1.0        6.12000000   5.000000e-012            anti-Omega_b+       -5332   0.000000e+000"
  , "Xi_bc0              522        5142  0.0        6.9          5.000000e-012                   Xi_bc0        5142   0.000000e+000"
  , "Xi_bc~0             523       -5142  0.0        6.9          5.000000e-012              anti-Xi_bc0       -5142   0.000000e+000"
  , "Xi_bc+              532        5242  1.0        6.9          5.000000e-012                   Xi_bc+        5242   0.000000e+000"
  , "Xi_bc~-             533       -5242 -1.0        6.9          5.000000e-012              anti-Xi_bc-       -5242   0.000000e+000"
  , "Omega_bc0           544        5342  0.0        7.19099000   5.000000e-012                  unknown        5342   0.000000e+000"
  , "Omega_bc~0          545       -5342  0.0        7.19099000   5.000000e-012                  unknown       -5342   0.000000e+000"
  , "Omega_bcc+          562        5442  1.0        8.30945000   5.000000e-012                  unknown        5442   0.000000e+000"
  , "Omega_bcc~-         563       -5442 -1.0        8.30945000   5.000000e-012                  unknown       -5442   0.000000e+000"
  , "Xi_bb-              568        5512 -1.0       10.42272000   5.000000e-012                  unknown        5512   0.000000e+000"
  , "Xi_bb~+             569       -5512  1.0       10.42272000   5.000000e-012                  unknown       -5512   0.000000e+000"
  , "Xi_bb0              572        5522  0.0       10.42272000   5.000000e-012                  unknown        5522   0.000000e+000"
  , "Xi_bb~0             573       -5522  0.0       10.42272000   5.000000e-012                  unknown       -5522   0.000000e+000"
  , "Omega_bb-           576        5532 -1.0       10.60209000   5.000000e-012                  unknown        5532   0.000000e+000"
  , "Omega_bb~+          577       -5532  1.0       10.60209000   5.000000e-012                  unknown       -5532   0.000000e+000"
  , "Omega_bbc0          580        5542  0.0       11.70767000   5.000000e-012                  unknown        5542   0.000000e+000"
  , "Omega_bbc~0         581       -5542  0.0       11.70767000   5.000000e-012                  unknown       -5542   0.000000e+000"
  , "b-hadron            344          85 -0.3          5.000000   5.000000e-012                 b-hadron          85   0.000000e+000"
  , "anti-b-hadron       345         -85  0.3          5.000000   5.000000e-012            anti-b-hadron         -85   0.000000e+000"
  ]

