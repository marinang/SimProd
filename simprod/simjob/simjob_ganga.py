#!/usr/bin/python
import os

from .utils import baserunnumber
from .setup import DoProd, checksiminputs

DEBUG = 0

class GangaSimJob(object):
    """
    Ganga simulation job
    """
    
    def __init__(self, **kwargs):		
        self.subjobs = {}
       
        self._nevents = kwargs.get('nevents', None)
        if self._nevents is None:
            raise ValueError("Please set nevents!")
        self._neventsjob = kwargs.get('neventsjob', 50)
        self._year = kwargs.get('year', None)
        if self._year is None:
            raise ValueError("Please set year!")
        self._polarities = kwargs.get('polarities', None)
        self._simcond = kwargs.get('simcond', "Sim09g")
        self._stripping = kwargs.get('stripping', None)
        self._turbo = kwargs.get('turbo', False)
        self._mudst = kwargs.get('mudst', False)
        self._runnumber = kwargs.get('runnumber', baserunnumber())
        self._decfiles = kwargs.get('decfiles', 'v30r25')
        self._inscreen = kwargs.get('inscreen', False)
        self._keeplogs = kwargs.get('keeplogs', True)
        self._keepxmls = kwargs.get('keepxmls', True)
        self._redecay = kwargs.get('redecay', False)
        self._simmodel = kwargs.get('simmodel', "pythia8")
                        
        self._evttype = kwargs.get('evttype', None)	
        if self._evttype is None:
            raise ValueError("Please set evttype!")
        else:
            self.__setoptfile()
        
    @property
    def range_subjobs(self):
        for n in range(self.nsubjobs):
            yield n + 1
                                    
    @property
    def nevents( self):
            return self._nevents
            
    @nevents.setter
    def nevents(self, value):
        if isinstance(value, (int, float)):
            self._nevents = int(value)
        else:
            raise TypeError("nevents must be a int!")
                    
    @property
    def neventsjob( self):
        return self._neventsjob
            
    @neventsjob.setter
    def neventsjob(self, value):
        if isinstance(value, (int, float) ):
            self._neventsjob = int(value)
        else:
            raise TypeError("nevents must be a int!")
                    
    @property
    def nsubjobs(self):
        self._nsubjobs = int( self.nevents/ self.neventsjob )		
        return self._nsubjobs
            
    @property
    def evttype(self):
        return self._evttype
            
    @evttype.setter
    def evttype(self, value):
        self._evttype = value		
        self.__setoptfile()
            
    @property	
    def simcond(self):
        return self._simcond
            
    @simcond.setter	
    def simcond(self, value):
        if not isinstance(value, str):
            raise TypeError("simcond must be a str!")
        if not value in ["Sim09b", "Sim09c", "Sim09e", "Sim09f"]:
            raise ValueError("simcond must be Sim09b, Sim09c, Sim09d or Sim09f!")
        self._simcond = value
            
    @property	
    def simmodel(self):
        return self._simmodel
            
    @simmodel.setter	
    def simmodel(self, value):
        if not isinstance(value, str):
            raise TypeError("simmodel must be a str!")
        if not value in ["pythia8", "BcVegPy"]:
            raise ValueError("simmodel must be pythia8 or BcVegPy!")
        self._simmodel = value
            
    @property
    def doprod(self):
        return DoProd(self.simcond, self.year)
            
    @property	
    def stripping(self):
        return self._stripping
            
    @stripping.setter	
    def stripping(self, value):
        if not isinstance(value, str):
            raise TypeError("simcond must be a str!")
        if not value in ["21", "24", "28", "24r1", "24r1p1", "28r1", "28r1p1", "29r2", "34", "34r0p1"]:
            raise ValueError("stripping must be '21, '24', '28', '24r1', '24r1p1', '28r1', '28r1p1', '29r2', '34' or '34r0p1'!")
        self._stripping = value
            
    @property	
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
                raise TypeError("nevents must be a int!")
        if not value in [2011,2012,2015,2016,2017,2018]:
                raise ValueError("year must be 2011, 2012, 2015, 2016, 2017 or 2018!")
        self._year = value
            
    @property
    def keys(self):
        return self.subjobs.keys()
                        
    @property	
    def destdir(self):
        self._destdir = "{0}/{1}/{2}/{3}".format(self.options["basedir"], self.evttype, self.year, self.simcond)
        if self._redecay:
            self._destdir += "_ReDecay"
        return self._destdir
            
    @property	
    def optfile(self):
            return self._optfile
            
    @property	
    def turbo(self):
            return self._turbo
            
    @turbo.setter	
    def turbo(self, value):
        if isinstance(value, bool):
            self._turbo = value
        else:
            raise TypeError("turbo must be set to True/False!")
                    
    @property	
    def mudst(self):
        return self._mudst
            
    @mudst.setter	
    def mudst(self, value):
        if isinstance(value, bool):
            self._mudst = value
        else:
            raise TypeError("mudst must be set to True/False!")
                    
    @property
    def keeplogs(self):
        return self._keeplogs
            
    @keeplogs.setter	
    def keeplogs(self, value):
        if isinstance(value, bool):
            self._keeplogs = value			
        else:
            raise TypeError("keeplogs must be set to True/False!")
                    
    @property
    def keepxmls(self):
        return self._keepxmls
            
    @keepxmls.setter	
    def keepxmls(self, value):
        if isinstance(value, bool):
            self._keepxmls = value			
        else:
            raise TypeError("keepxmls must be set to True/False!")
                    
    @property
    def redecay(self):
        return self._redecay
            
    @redecay.setter	
    def redecay(self, value):
        if isinstance(value, bool):
            self._redecay = value
        else:
            raise TypeError("redecay must be set to True/False!")
                    
    def getrunnumber(self, job_number = None ):
        if job_number != None and not isinstance(job_number, int):
            raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(job_number.__class__.__name__))
        
        if job_number == None:
            return self._runnumber
        else:
            return self._runnumber + job_number
                    
    def prepare(self, **kwargs):
        if len(self.subjobs) < 1:
                                
            if not self._evttype:
                raise ValueError('Evttype not defined!')
                    
            if not self._nevents:
                raise ValueError('nevents not defined!')
                    
            if not self._neventsjob:
                raise ValueError('neventsjob not defined!')
                    
            if not self._year:
                raise ValueError('year not defined!')
                    
            if not self._simcond:
                raise ValueError('simcond not defined!')
                    
            checksiminputs(self)
            
            if self.nsubjobs  == 0:
                self.neventsjob = int(self.nevents / 2)
                self.nevents    = self.neventsjob * 2
    
            def sample_polarities():
                polarities = ["MagUp", "MagDown"]
                i = randint(0, 1)
                p1 = polarities.pop(i)
                p2 = polarities[0]
                
                polarity = [p1 for i in range(1, int(self.nsubjobs / 2) + 1)]
                polarity += [p2 for i in range(int(self.nsubjobs / 2) + 1, self.nsubjobs + 1)]
                return shuffle(polarity)
                                    
            if not isinstance(self._polarities, list):
                if self._polarities is None:
                    self._polarities = sample_polarities()
                elif self._polarities in ["MagUp", "MagDown"]:
                    self._polarities = [self._polarities for i in self.range_subjobs]
                else:
                    raise ValueError()
            else:
                if len(self._polarities) != self.nsubjobs:
                    self._polarities = sample_polarities()
                elif not all(p in ["MagUp", "MagDown"] for p in self._polarities):
                    raise ValueError()
                                                                                                                                        
        infiles = kwargs.get('infiles', [])
                        
        for n in self.range_subjobs:				
            if self.subjobs.get(n, None) is not None:
                continue
                    
            self._preparesubjobs(n, infiles=infiles)

    def _preparesubjobs( self, sjn, **kwargs ):
        if DEBUG > 2:
            print(sjn)
                                        
        if self._polarities:	
                polarity  = self._polarities[sjn-1]
        else:
                if sjn <= int(self.nsubjobs/2):
                        polarity = "MagUp"
                else:
                        polarity = "MagDown"
                        
        if sjn not in self.keys:
                runnumber = self.getrunnumber(sjn)
                self.subjobs[sjn] = SimulationSubJob( parent=self, polarity=polarity, runnumber=runnumber, subjobnumber=sjn, **kwargs )	
    
    def cancelpreparation( self, **kwargs ):	
        for n in self.range_subjobs:				
            if self.subjobs.get(n, None):
                del self.subjobs[n]

    def __getitem__(self, sjob_number):
        return self.subjobs[sjob_number]
            
    def __setitem__(self, sjob_number, subjob):
        self.subjobs[sjob_number] = subjob
            
    def __iter__(self):
        for n in self.range_subjobs:
            yield self[n]
                    
    def __setoptfile( self ):
        moddir = os.getenv("SIMPRODPATH")
        self._optfile = "{0}/EvtTypes/{1}/{1}.py".format( moddir, self._evttype )

        if not os.path.isfile( self._optfile ):
            getevttype( evttype = self._evttype, decfiles = self._decfiles )
                    
                                    
      
                            

