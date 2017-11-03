from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
