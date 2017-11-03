"""
A few common methods for extracting particle properties from SLHA spectrum and decay files
"""
__author__ = "Pieter David <pieter.david@cern.ch>"
__date__   = "2013-08-28"

def getTotalWidthFromSLHA( slhaFileName, particle ):
    """
    Extract the total width (in GeV) of particle from the decay table in the SLHA file
    """
    W = 0.
    with open(slhaFileName, "read") as spcFile:
       for ln in spcFile:
           if "DECAY" in ln.upper() and particle in ln:
               tokens = ln.strip().split()
               if len(tokens) >= 3:
                   W = float(tokens[2])
    return W

def getMassesFromSLHA( slhaFileName ):
    """
    Collect all masses (in GeV) from a SLHA file

    Return: { str(pid) : mass }
    """
    inMassBlock = False
    masses = dict()
    with open(slhaFileName, "read") as spcFile:
        for ln in spcFile:
            if not ln.strip().startswith("#"):
                if inMassBlock:
                    if ln.upper().startswith("BLOCK"): ## check if the block ended
                        inMassBlock = False
                    else:
                        tokens = ln.strip().split()
                        masses[tokens[0]] = float(tokens[1])
                elif ln.strip().upper().startswith("BLOCK") and ln.strip().split()[1].upper() == "MASS":
                    inMassBlock = True
    return masses

def getParticlePropertiesAndPythia8Commands(spcFileName, partNames):
    """
    Extract mass and width for particles in partNames from filename

    Returns: { str(pid) : ( mass[GeV] , tau[s] ) }, [ pythia8 tau0 commands ]
    """
    import os.path
    slhaFileName = os.path.expandvars(spcFileName)
    try:
        from pyslha import readSLHAFile
        blocks, decays = readSLHAFile(slhaFileName)
        massesAndWidthsInGeV = dict( (part, ( blocks["MASS"][int(part)] , decays[int(part)].totalwidth) ) for part in partNames )
    except:
        massesInGeV = getMassesFromSLHA(slhaFileName)
        massesAndWidthsInGeV = dict( (part, ( massesInGeV.get(part) , getTotalWidthFromSLHA(slhaFileName, part)) ) for part in partNames )
    from GaudiKernel import SystemOfUnits as units
    from GaudiKernel import PhysicalConstants as constants
    pps = dict()
    pythiaCommands = list()
    for part in partNames:
        massInGeV, widthInGeV = massesAndWidthsInGeV[part]
        pps[part] = ( massInGeV, constants.hbar_Planck / ( widthInGeV*units.GeV ) / units.second) # (mass [GeV], lifetime [s])
        pythiaCommands.append("%s:tau0 = %e" % ( part , constants.hbarc / ( widthInGeV*units.GeV ) / units.mm ) ) # lifetime in mm/c
    return pps, pythiaCommands
