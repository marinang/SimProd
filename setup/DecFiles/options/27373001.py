# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27373001.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 27373001
#
# ASCII decay Descriptor: [D*+ -> (D0 -> mu+ e-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27373001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,mue=LooseCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/LooseCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'LooseCut' ) 
# 
looseCut = gen.SignalPlain.LooseCut
looseCut.Decay     = '[ D*(2010)+ -> ^( D0 => ^(mu+|e+) ^(mu-|e-) ) ^pi+ ]CC'
looseCut.Cuts      =    {
    '[mu-]cc' : 'goodMuon'     ,
    '[D0]cc'  : 'goodD0' }
looseCut.Preambulo += [
    'inAcc        = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon     = ( GPT > 0.70 * GeV ) & ( GP > 3.80 * GeV ) & inAcc' ,
    'goodD0       = ( GPT > 1.60 * GeV )' ]



# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/LooseCut"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 413,-413 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_413.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 27373001
