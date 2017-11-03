# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12103240.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 12103240
#
# ASCII decay Descriptor: [B+ -> (K_1+ -> K+ pi- pi+) gamma]cc
#
from Configurables import Generation
Generation().EventType = 12103240
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Kpipigamma=HighPtGamma,TightCut,mKpipiFlat.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[B+ => ^( K_1(1270)+ -> ^K+ ^pi- ^pi+) ^gamma]CC'
tightCut.Cuts      =    {
    '[B+]cc'    : ' goodB     ' , 
    '[K+]cc'    : ' goodTrack ' , 
    '[pi+]cc'   : ' goodTrack ' , 
    'gamma'     : ' goodGamma ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 )       ' ,
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5            ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5            ' ,
    'goodB     = ( GBEAUTY )                               ' ,
    'goodTrack = ( GPT >  250. * MeV ) & inAcc             ' ,
    'goodGamma = ( GPT > 2000. * MeV ) & inEcalX & inEcalY ' ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

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
pgun.EventType = 12103240
