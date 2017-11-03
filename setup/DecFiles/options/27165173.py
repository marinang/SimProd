# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165173.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 27165173
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27165173
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KSKS=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
#gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
#tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut = gen.SignalPlain.TightCut
#tightCut.Decay     = '[^D*(2010)+ ==> (^(D0 ==> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-))^pi+)]CC'
tightCut.Decay     = '^[ D*(2010)+ ==> ^( D0 ==> ^( KS0 => ^pi+ ^pi- ) ^( KS0 => ^pi+ ^pi- ) ) ^pi+]CC'
tightCut.Cuts      =    {
    '[D*(2010)+]cc'    : ' goodDst     ' , 
    '[D0]cc'    : ' goodD     ' , 
    'KS0'   : ' goodKs ' } 
#    '[pi+]cc'   : ' goodTrack ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.010 , GTHETA , 0.300 ) ' , 
    'goodDst     = ( GP > 20 * GeV ) & (GCHILD(GTHETA,2) > 0.01) & (GCHILD(GTHETA,2) < 0.3)     ' , 
    'goodD     = ( GP > 10 * GeV ) & switch(GCHILD(GPT,1) < GCHILD(GPT,2), (GCHILD(GPT,1) > 300) & (GCHILD(GPT,2) > 800), (GCHILD(GPT,1) > 800) & (GCHILD(GPT,2) > 300)) & inAcc            ' , 
    'goodTrack = ( GP >  2.0 * GeV ) & (GPT >  100 * MeV )       ' , 
    'goodKs   = ( GP >  4 * GeV) & inAcc & (GFAEVX( abs( GVZ  ) , 0 ) < 2500 * mm) & (GCHILD(GPT,1) > 100 * MeV) &  (GCHILD(GPT,2) > 100 * MeV) &  (GCHILD(GP,1) > 2.0 * GeV) &  (GCHILD(GP,2)  > 2.0 * GeV)        ' ] 



# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

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
pgun.EventType = 27165173
