# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42901000.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 42901000
#
# ASCII decay Descriptor: pp -> (W-> tau (mu nu_tau nu_mu) nu_tau) (b b~) or pp -> (W-> tau (el nu_tau nu_el) nu_tau) (b b~)...
#
from Configurables import Generation
Generation().EventType = 42901000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_taunubbtau=lep.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/OneLepFromTau"

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "wbb",
'alpgen_ihvy' : 5,
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : 1.596, # theta' : 400 mrad
'alpgen_ptbmin' : 3.0,
'alpgen_drbmin' : 0.500,
'alpgen_etabmax' : 10.0,
'alpgen_eta1lmin' : -9999, # no eta cuts on the tau (will be in the muon)
'alpgen_ptlmin' : 10.0,
'alpgen_drlmin' : 0.,
'alpgen_etalmax' : 9999.0, # no eta cuts on the tau (will be in the muon)
'alpgen_iwdecmode' : 3,
'alpgen_ndns' : 9,
}

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "OneLepFromTau" )
tracksInAcc = Generation().OneLepFromTau
tracksInAcc.Code = " ( count ( isGoodMu ) > 0 )"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodMu   = ( (  'W+' == GABSID ) & GINTREE( 15 == GABSID ) & GINTREE( ((13 == GABSID) | (11 == GABSID)) & ( GTHETA < 400.0*mrad ) & ( GPT > 10*GeV ) ) )"
   ]

