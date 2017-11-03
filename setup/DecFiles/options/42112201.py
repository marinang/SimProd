# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42112201.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 42112201
#
# ASCII decay Descriptor: pp -> [Z -> (Upsilon -> mu+ mu-) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42112201
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_Upsilongamma=DecProdCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"


from Configurables import LoKi__FullGenEventCut 
Generation().addTool(LoKi__FullGenEventCut, "ParsInAcc") 
ParsInAcc = Generation().ParsInAcc

ParsInAcc.Code = "(count(isGoodZ) > 0)"

ParsInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import millimeter, micrometer, MeV, GeV"
   , "inCaloAcc    = (in_range(0.030, abs(GPX/GPZ), 0.300) & in_range(0.030, abs(GPY/GPZ), 0.250) & (GPZ > 0))"
   , "inAcc        = (in_range(0.030, GTHETA, 0.400))"
   , "NGoodMuonm   = (GINTREE(( (('mu-' == GID)) & (GPT > 0.3*GeV) & inAcc)))"
   , "NGoodMuonp   = (GINTREE(( (('mu+' == GID)) & (GPT > 0.3*GeV) & inAcc)))"
   , "NGoodUpsilon = (NGoodMuonm & NGoodMuonp)"
   , "NGoodGamma   = GINTREE(('gamma' == GABSID) & (GPT > 10.0*GeV) & inCaloAcc)"
   , "isGoodZ      = (('Z0' == GABSID) & NGoodGamma & NGoodUpsilon)" 
   ]

# Pythia8 options.
from Gaudi.Configuration import importOptions
from Configurables import Pythia8Production
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    'WeakSingleBoson:ffbar2gmZ = on',
    'WeakZ0:gmZmode = 2',
    '23:mayDecay = false']


