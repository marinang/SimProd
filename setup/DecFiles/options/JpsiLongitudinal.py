from Configurables import ToolSvc , EvtGenDecay
ToolSvc().addTool( EvtGenDecay )

ToolSvc().EvtGenDecay.PolarizedCharmonium = True
ToolSvc().EvtGenDecay.RealHelOne = 0.
ToolSvc().EvtGenDecay.RealHelZero = 1.


