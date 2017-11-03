"""

Based on 42100001, but now with harsh fiducial cut to save space.

- Has both Z/gamma* comtribution
- Mass cut > 40
- Tau lepton in (wide) acceptance, PT>18GeV
- Let Pythia8 handle tau decay.
- Decay of tau lepton has high-PT, varies by channel
  - ee, emu, mumu: 13 GeV + 3 GeV
  - eh1, muh1: lepton 13GeV, hadron 8GeV
  - eh3, muh3: lepton 13GeV, 3-prongs (5,,0.5) GeV
  - h1h1: both 8GeV
  - h1h3: h1 8GeV, h3 like above
  - h3h3: both h3 like above

Note: Be careful of the generator efficiency value since it's different
between each di-tau channel. Thus this sample is not suitable to study the 
acceptance efficiency, but only after.
Need `${XMLSUMMARYKERNELROOT}/options/add-XMLSummary.py` to return the list of
geneff for each ditau channel.

"""

from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

## Inherit from plain Zgtautau
importOptions( "$DECFILESROOT/options/Zgtautau.py" )

## Allow Pythia to handle tau decays (not EvtGen through TAUOLA).
from Configurables import PythiaHiggsType
Generation().Special.CutTool = "PythiaHiggsType"
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.TypeOfLepton = [ "tau+" ]
Generation().Special.DecayTool = ""

## Prepare the cut on di-tau decay
preambulo_baseditau = """
# use descendants to allow tau recoiling. Use with care.
def WithOne(cut):
  from LoKiGen.decorators import GNINTREE, HepMC
  return (GNINTREE(cut, HepMC.descendants) >= 1)
def WithTwo(cut):
  from LoKiGen.decorators import GNINTREE, HepMC
  return (GNINTREE(cut, HepMC.descendants) >= 2)
#
# Channel counter: Forget about kinematic. Look on topology only.
IsTau       = (GABSID == 15)
IsMuon      = (GABSID == 13)
IsElec      = (GABSID == 11)
IsHad       = (GHADRON & GCHARGED)
IsTauMu     = IsTau & (GNINTREE(IsMuon)==1)
IsTauE      = IsTau & (GNINTREE(IsElec)==1)
IsTauH1     = IsTau & (GNINTREE(IsHad)==1)
IsTauH3     = IsTau & (GNINTREE(IsHad)==3)
IsDitau     = (GNINTREE(IsTau)==2) # don't search in descendants unlike other.
IsDitauEE   = WithTwo(IsTauE)
IsDitauEH1  = WithOne(IsTauE) & WithOne(IsTauH1)
IsDitauEH3  = WithOne(IsTauE) & WithOne(IsTauH3)
IsDitauEMU  = WithOne(IsTauE) & WithOne(IsTauMu)
IsDitauH1H1 = WithTwo(IsTauH1)
IsDitauH1H3 = WithOne(IsTauH1) & WithOne(IsTauH3)
IsDitauH1MU = WithOne(IsTauH1) & WithOne(IsTauMu)
IsDitauH3H3 = WithTwo(IsTauH3)
IsDitauH3MU = WithOne(IsTauH3) & WithOne(IsTauMu)
IsDitauMUMU = WithTwo(IsTauMu)
moni = (
  select(IsDitau)
  >> process(monitor(IsDitauEE   , 'ee'    , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauEH1  , 'eh1'   , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauEH3  , 'eh3'   , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauEMU  , 'emu'   , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauH1H1 , 'h1h1'  , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauH1H3 , 'h1h3'  , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauH1MU , 'h1mu'  , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauH3H3 , 'h3h3'  , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauH3MU , 'h3mu'  , LoKi.Monitoring.ContextSvc)) 
  >> process(monitor(IsDitauMUMU , 'mumu'  , LoKi.Monitoring.ContextSvc)) 
  >> (GSIZE>-1)
)
""".split('\n')

## More cut on tau product
from Configurables import LoKi__FullGenEventCut
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/DitauCondensed"
Generation().addTool( LoKi__FullGenEventCut, name='DitauCondensed' )
cut = Generation().DitauCondensed
cut.Code = "(moni) & (count(GoodDitau) >= 1)"
cut.Preambulo += preambulo_baseditau + """
from GaudiKernel.SystemOfUnits import GeV, mrad
VRAND         = (GONE>>XRAND)
InWideAcpt    = (GTHETA < 360.0*mrad)  # 1.7
GoodMuon      = IsMuon & InWideAcpt
GoodElec      = IsElec & InWideAcpt
GoodHadron    = IsHad  & InWideAcpt
GoodTauMu_3   = IsTau & (GNINTREE( GoodMuon & (GPT> 3*GeV) )==1)
GoodTauMu_13  = IsTau & (GNINTREE( GoodMuon & (GPT>13*GeV) )==1)
GoodTauE_3    = IsTau & (GNINTREE( GoodElec & (GPT> 3*GeV) )==1)
GoodTauE_13   = IsTau & (GNINTREE( GoodElec & (GPT>13*GeV) )==1)
GoodTauH1_8   = IsTau & (GNINTREE(GoodHadron)==1) & (GNINTREE(GoodHadron&(GPT>8*GeV))==1)
GoodTauH1_3   = IsTau & (GNINTREE(GoodHadron)==1) & (GNINTREE(GoodHadron&(GPT>3*GeV))==1)
GoodTauH3     = IsTau & (GNINTREE(GoodHadron)==3) & (GNINTREE(GoodHadron&(GPT>5*GeV))>=1) & (GNINTREE(GoodHadron&(GPT>0.5*GeV))==3)
GoodDitauEE   = WithOne(GoodTauE_13)  & WithTwo(GoodTauE_3)
GoodDitauEH1  = WithOne(GoodTauE_13)  & WithOne(GoodTauH1_8)
GoodDitauEH3  = WithOne(GoodTauE_13)  & WithOne(GoodTauH3)
GoodDitauEMU  = (WithOne(GoodTauE_13) & WithOne(GoodTauMu_3)) | (WithOne(GoodTauE_3) & WithOne(GoodTauMu_13))
GoodDitauH1H1 = WithTwo(GoodTauH1_8)
GoodDitauH1H3 = WithOne(GoodTauH1_8)  & WithOne(GoodTauH3)
GoodDitauH1MU = WithOne(GoodTauMu_13) & WithOne(GoodTauH1_8)
GoodDitauH3H3 = WithTwo(GoodTauH3)
GoodDitauH3MU = WithOne(GoodTauMu_13) & WithOne(GoodTauH3)
GoodDitauMUMU = WithOne(GoodTauMu_13) & WithTwo(GoodTauMu_3)
GoodDitauType = (GoodDitauEE)|(GoodDitauEH1)|(GoodDitauEH3)|(GoodDitauEMU)|(GoodDitauH1H1)|(GoodDitauH1H3)|(GoodDitauH1MU)|(GoodDitauH3H3)|(GoodDitauH3MU)|(GoodDitauMUMU)
GoodDitau     = (IsDitau) & (GoodDitauType)
""".split('\n')


## Post-filter monitoring
from Configurables import GaudiSequencer
from Configurables import LoKi__VoidFilter
algo = LoKi__VoidFilter('DiTauAftercut')
algo.Code      = 'GSOURCE() >> moni'
algo.Preambulo = preambulo_baseditau
GaudiSequencer("GenMonitor").Members += [algo]
