# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15144003.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15144003
#
# ASCII decay Descriptor: [ ( Lambda_b0  ->   p+ K- (mPsi -> mu+ mu-) )]CC
#
from Configurables import Generation
Generation().EventType = 15144003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKmumu=phsp,Highq2,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "mPsi 853   9030443 0 3.800 1.65e-24 mPsi 0 0" ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ ^( Lambda_b0  ->   ^p+ ^K- ^( mPsi -> ^mu+ ^mu- ) )]CC'
tightCut.Cuts      =    {
    '[mu+]cc'             : ' inAcc  ' ,
    '[K+]cc'              : ' inAcc  ' ,
    '[p+]cc'              : ' inAcc  ' ,
    '[Lambda_b0]cc'       : ' highq2   ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    "highq2    = ( ( GMASS ( 'mu+' == GID , 'mu-' == GID ) ) > 3200 * MeV )  " ]


