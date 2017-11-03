from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV, MeV, mm

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  100
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = False
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 2.9*GeV 
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 2.9*GeV 
#Generation().DiLeptonInAcceptance.MinMass = 10*MeV
Generation().DiLeptonInAcceptance.MaxMass = 4500*MeV
Generation().DiLeptonInAcceptance.PreselDoca = True
Generation().DiLeptonInAcceptance.DocaCut = 0.35*mm
Generation().DiLeptonInAcceptance.PreselPtProd = True
Generation().DiLeptonInAcceptance.LeptonOnePtMin = 0.28
Generation().DiLeptonInAcceptance.LeptonTwoPtMin = 0.28

#Generation().DiLeptonInAcceptance.PtMinCut = 0.25*GeV
#Generation().DiLeptonInAcceptance.PtProdMaxCut = 1000*GeV*1000*GeV
