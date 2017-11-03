from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().DiLeptonInAcceptance.LeptonIDOne = 11
Generation().DiLeptonInAcceptance.LeptonIDTwo = 11

