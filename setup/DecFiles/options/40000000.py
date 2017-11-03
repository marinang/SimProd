# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40000000.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 40000000
#
# ASCII decay Descriptor: pp -> b b~ b b~
#
from Configurables import Generation
Generation().EventType = 40000000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_4b_AlpGen.dec"
Generation().Special.CutTool = ""

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "4b",
'alpgen_ihvy' : 5,
'alpgen_ihvy2' : 5,
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : 1.596,                                                
'alpgen_etabmax' : 10.0,                                                  
'alpgen_ptbmin' : 2.0, # all b quarks must have pt > 2.0 GeV         
'alpgen_pt2bmin' : 2.5, #at least 2 b quarks must have pt > 2.5 GeV 
'alpgen_pt1bmin' : 2.5, #at least 1 b quark must have pt > 2.5 GeV
'alpgen_eta2bmin': 2, #at least two b with a mininum eta of 2
'alpgen_drbmin' : 0.,
'alpgen_etabmax' : 10.0,
'alpgen_ndns' : 9,
}

