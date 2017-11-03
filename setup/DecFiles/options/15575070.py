# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15575070.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 15575070
#
# ASCII decay Descriptor: [ Lambda_b0 -> (D*+ -> (D0 -> K- pi+) pi+) anti-nu_mu mu- n0]cc
#
from Configurables import Generation
Generation().EventType = 15575070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_n0Dstmunu,Dst=D0pi,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
                                                                                                    
#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalPlain.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalPlain.TightCut
tightCut.Decay = '^[ [Lambda_b0]cc => ^(D*(2010)+ ==> ^(D0 ==> ^K- ^pi+) ^pi+) ^n0 ^mu- ^nu_mu~ ]CC'

tightCut.Preambulo += [
        'inAcc        = (in_range(0.005, GTHETA, 0.400))',
        'GVZ = LoKi.GenVertices.PositionZ()',
        'from GaudiKernel.SystemOfUnits import millimeter',
        'goodMu       = (GPT > 700 * MeV)  & (GP > 2.0*GeV) & inAcc',
        'goodK        = (GPT > 300 * MeV)  & (GP > 2.0*GeV) & inAcc',
        'goodpi       = (GPT > 300 * MeV)  & (GP > 2.0*GeV) & inAcc',
        'goodD        = (GPT > 1200 * MeV)',
        'goodB        = (GFAEVX(abs(GVZ), 0) - GFAPVX(abs(GVZ), 0) > .5 * millimeter)'
        ]
tightCut.Cuts = {
    '[Lambda_b0]cc': 'goodB',
    '[D*(2010)-]cc': 'goodD',
    '[D~0]cc'      : 'goodD',
    '[K+]cc'       : 'goodK',
    '[pi+]cc'      : 'goodpi',
    '[mu+]cc'      : 'goodMu'
    }

