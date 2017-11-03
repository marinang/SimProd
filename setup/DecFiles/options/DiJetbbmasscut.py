from Configurables import LoKi__InvariantMassQQMCJets, Generation

Generation().FullGenEventCutTool = "LoKi::InvariantMassQQMCJets/InvariantMassDiJet"
Generation().addTool( LoKi__InvariantMassQQMCJets, "InvariantMassDiJet" )
InvariantMassDiJet = Generation().InvariantMassDiJet
InvariantMassDiJet.Code = " count ( GBEAUTY ) >= 0 "


from GaudiKernel.SystemOfUnits import  GeV

InvariantMassDiJet.MinMassqq  = 75*GeV
InvariantMassDiJet.MaxMassqq  = 300*GeV
InvariantMassDiJet.QuarkOneID = 5
InvariantMassDiJet.QuarkTwoID = -5

