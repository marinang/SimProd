# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40000010.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 40000010
#
# ASCII decay Descriptor: pp -> c c~ c c~
#
from Configurables import Generation
Generation().EventType = 40000010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_4c_AlpGen.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "4b", ## needed to cope with Alpgen opts
'alpgen_ihvy' : 4, ## 2c
'alpgen_ihvy2' : 4, ## 2 more c
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : -9999., # no cut applied
'alpgen_etabmax' : 9999., # no cut applied
'alpgen_ptbmin' : 0, # no cut applied
'alpgen_pt2bmin' : 0, # no cut applied
'alpgen_pt1bmin' : 0, # no cut applied
'alpgen_eta2bmin': -9999., # no cut applied
'alpgen_drbmin' : 0., # no cut applied
'alpgen_etabmax' : 9999., # no cut applied
'alpgen_ndns' : 9,
}

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsTypeCut" )
tracksInAcc = Generation().HiggsTypeCut
tracksInAcc.Code = " (count ( isGoodCharm)>1 )"                  
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                            
   , "isGoodCharm   = ((  'c' == GABSID ) & GINTREE( GCHARM & ( GTHETA < 400.0*mrad ) & (GTHETA > 15.0*mrad )& (GPT > 2.0*GeV)))"
   ]
                                                                                              

