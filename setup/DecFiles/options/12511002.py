# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12511002.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 12511002
#
# ASCII decay Descriptor: [B+ -> mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 12511002
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_munu=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/MuonCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]
                                                                    
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "MuonCut" )
MuonCut = Generation().MuonCut                                                      
MuonCut.Code = " ( count ( isGoodB ) > 0 ) "                                          
                                                                                        
MuonCut.Preambulo += [                                                                                          
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB     = ((  521 == GABSID ) & (GNINTREE( (  'mu+' == GABSID ) & (GPT > 4 * GeV) & ( GTHETA < 400 * mrad )) > 0))"
   ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = ""

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12511002
