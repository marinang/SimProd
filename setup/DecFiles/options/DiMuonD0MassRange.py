from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV, MeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  50
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 5*GeV 
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 5*GeV
Generation().DiLeptonInAcceptance.LeptonOnePtMin = 750*MeV
Generation().DiLeptonInAcceptance.LeptonTwoPtMin = 750*MeV
Generation().DiLeptonInAcceptance.MinMass = 1760*MeV
Generation().DiLeptonInAcceptance.MaxMass = 1960*MeV

