from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV, MeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  50
Generation().addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = False
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV 
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
Generation().DiLeptonInAcceptance.MinMass = 4700*MeV
