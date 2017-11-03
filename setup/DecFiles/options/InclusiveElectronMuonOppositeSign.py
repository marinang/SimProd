from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.LeptonIDOne = 11 
Generation().DiLeptonInAcceptance.LeptonIDTwo = 13
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False

