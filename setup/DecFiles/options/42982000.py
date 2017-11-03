# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42982000.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 42982000
#
# ASCII decay Descriptor: pp -> (Z-> el el) (c c~)...
#
from Configurables import Generation
Generation().EventType = 42982000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_eecc_AlpGen.dec"
Generation().Special.CutTool = ""

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "zcc",
'alpgen_ihvy' : 4,
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : 1.596, # theta' : 400 mrad
'alpgen_ptcmin' : 3.0,
'alpgen_drcmin' : 0.1,
'alpgen_etacmax' : 10, # theta' : 0.15mrad
'alpgen_eta1lmin' : 1.596,
'alpgen_ptlmin' : 10.0,
'alpgen_drlmin' : 0.,
'alpgen_etalmax' : 10.0,
'alpgen_izdecmode' : 1,
'alpgen_ndns' : 9,
}


