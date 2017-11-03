from Configurables import ToolSvc , EvtGenDecay
ToolSvc().addTool( EvtGenDecay )

ToolSvc().EvtGenDecay.PolarizedCharmonium = True
ToolSvc().EvtGenDecay.RealHelOne = 1.0 
ToolSvc().EvtGenDecay.RealHelZero = 0.

