from Configurables import Generation, RepeatDecay, DiLeptonInAcceptance, Inclusive
from GaudiKernel.SystemOfUnits import GeV, MeV

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay )
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance )
Generation().DiLeptonInAcceptance.LeptonIDOne = 11 
Generation().DiLeptonInAcceptance.LeptonIDTwo = 13
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
Generation().DiLeptonInAcceptance.MinMass = 4600*MeV
Generation().DiLeptonInAcceptance.MaxMass = 7000*MeV
