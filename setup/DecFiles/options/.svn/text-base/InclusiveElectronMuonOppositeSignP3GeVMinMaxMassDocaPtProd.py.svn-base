from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV, MeV, mm

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  10
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().addTool( DiLeptonInAcceptance )
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().DiLeptonInAcceptance.LeptonIDOne = 11
Generation().DiLeptonInAcceptance.LeptonIDTwo = 13
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV
Generation().DiLeptonInAcceptance.MinMass = 4600*MeV
Generation().DiLeptonInAcceptance.MaxMass = 7000*MeV 
Generation().DiLeptonInAcceptance.PreselDoca = True
Generation().DiLeptonInAcceptance.DocaCut = 0.4*mm
Generation().DiLeptonInAcceptance.PreselPtProd = True
Generation().DiLeptonInAcceptance.PtProdMinCut = 1*GeV*1*GeV
Generation().DiLeptonInAcceptance.PtProdMaxCut = 4*GeV*4*GeV

