# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11876031.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11876031
#
# ASCII decay Descriptor: [B0 -> (D*- -> (anti-D0 -> K+ pi- pi+ pi-) pi-) mu+ nu_mu]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/D0muInAcc.py" )
from Configurables import Generation
Generation().EventType = 11876031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,Kpipipi=cocktail,hqet,MINT,D0muInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
