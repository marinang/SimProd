from Configurables import Generation
from GaudiKernel.SystemOfUnits import GeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().DiLeptonInAcceptance.LeptonIDOne = 11
Generation().DiLeptonInAcceptance.LeptonIDTwo = 11
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
Generation().DiLeptonInAcceptance.MinMass = 0*GeV
Generation().DiLeptonInAcceptance.MaxMass = 6.6*GeV
