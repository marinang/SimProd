from Configurables import Generation, RepeatDecay, DiLeptonInAcceptance, Inclusive
from GaudiKernel.SystemOfUnits import GeV, MeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  70
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
Generation().DiLeptonInAcceptance.MinMass = 4700*MeV
Generation().DiLeptonInAcceptance.MaxMass = 6000*MeV
