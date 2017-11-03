# Script to transform a EvtGen decay file into a
# human readable format.
# Usage : source setup.csh in cmt
#    python2.2 displayEvtTable.py [Name of decay file]
# It produces a .tex file output.tex which can then
# be processed with latex.

import os
import sys
import string
import re

pdgTable = { 'B0sig':511,'anti-B0sig':-511,'B+sig':521,'B-sig':-521,
             'B_s0sig':531,'anti-B_s0sig':-531,'B_c+sig':541,
             'B_c-sig':-541,'eta_bsig':551,'h_bsig':10553,
             'Sigma_b-sig':5112,'anti-Sigma_b+sig':-5112,
             'Lambda_b0sig':5122,'anti-Lambda_b0sig':-5122,'PYTHIA':999999 }
decayModels = ['BHADRONIC','BTO3PI_CP','BTO4PI_CP','BTOKPIPI_CP',
               'BSQUARK','BTO2PI_CP_ISO','BTOKPI_CP_ISO',
               'BTOXSETAP','BTOXSGAMMA','BTOXSLL','CB3PI-MPP',
               'CB3PI-P00','D_DALITZ','ETA_DALITZ','GOITY_ROBERTS',
               'HQET','HQET2','HELAMP','ISGW','ISGW2','KSTARNUNU',
               'KSTARSTARGAMMA','LNUGAMMA','MELIKHOV','OMEGA_DALITZ',
               'PARTWAVE','PHI_DALITZ','PHSP','PHOTOS','PI0_DALITZ','PYTHIA',
               'SLN','SLPOLE','SSD_CP','SSS_CP','SSS_CPT','SSS_CP_PNG',
               'STS','STS_CP','SVP_HELAMP','SVS','SVS_CP','SVS_CPLH',
               'SVS_CP_ISO','SVS_NONCPEIGEN','SVV_CP','SVV_CPLH',
               'SVV_HELAMP','SVV_NONCPEIGEN','SINGLE','SLL','TSS',
               'TVS_PWAVE','TAUHADNU','TAUSCALARNU','TAUVECTORNU',
               'TAULNUNU','VSP_PWAVE','VSS','VSS_BMIX','VSS_MIX','VVP',
               'VVS_PWAVE','VVPIPI','VECTORISR','VLL','VUB','BTOSLLALI',
               'BTOSLLBALL']
latexTable = { 1:'d',-1:'\\bar{d}',2:'u',-2:'\\bar{u}',3:'s',-3:'\\bar{s}',
               4:'c',-4:'\\bar{c}',5:'b',-5:'\\bar{b}',6:'t',-6:'\\bar{t}',
               11:'e^-',-11:'e^+',12:'\\nu_e',-12:'\\bar{\\nu_e}',
               13:'\\mu^-',-13:'\\mu^+',14:'\\nu_\\mu',-14:'\\bar{\\nu_\\mu}',
               15:'\\tau^-',-15:'\\tau^+',16:'\\nu_\\tau',
               -16:'\\bar{\\nu_\\tau}',
               22:'\\gamma',111:'\\pi^0',211:'\\pi^+',-211:'\\pi^-',
               541:'B_c^+',-541:'B_c^-',5212:'\\Sigma_b^0',
               -5212:'\\bar{\\Sigma}_b^0',5112:'\\Sigma_b^-',
               -5112:'\\bar{\\Sigma}_b^+',5222:'\\Sigma_b^+',
               -5222:'\\bar{\\Sigma}_b^-',5232:'\\Xi_b^0',
               -5232:'\\bar{\\Xi}_b^0',5132:'\\Xi_b^-',-5132:'\\bar{\\Xi}_b^+',
               5122:'\\Lambda_b^0',-5122:'\\bar{\\Lambda}_b^0',10443:'h_c(1P)',
               42:'X_u^+',-42:'X_u^-',41:'X_u^0',4334:'\\Omega_c^{*0}',
               -4334:'\\bar{\\Omega}_c^{*0}',4332:'\\Omega_c^0',
               -4332:'\\bar{\\Omega}_c^0',4324:'\\Xi_c^{*+}',
               -4324:'\\bar{\\Xi}_c^{*-}',4314:'\\Xi_c^{*0}',
               -4314:'\\bar{\\Xi}_c^{*0}',4224:'\\Sigma_c^{*++}',
               -4224:'\\bar{\\Sigma}_c^{*--}',4214:'\\Sigma_c^{*+}',
               -4214:'\\bar{\\Sigma}_c^{*-}',4114:'\\Sigma_c^{*0}',
               -4114:'\\bar{\\Sigma}_c^{*0}',-3334:'\\bar{\\Omega}^+',
               3334:'\\Omega^-',3314:'\\Xi^{*-}',-3314:'\\bar{\\Xi}^{*+}',
               3312:'\\Xi^-',-3312:'\\bar{\\Xi}^+',3322:'\\Xi^0',
               -3322:'\\bar{\\Xi}^0',3214:'\\Sigma^{*0}',
               -3214:'\\bar{\\Sigma}^{*0}',3224:'\\Sigma^{*+}',
               -3224:'\\bar{\\Sigma}^{*-}',3114:'\\Sigma^{*-}',
               -3114:'\\bar{\\Sigma}^{*+}',3212:'\\Sigma^0',
               -3212:'\\bar{\\Sigma}^0',3112:'\\Sigma^-',
               -3112:'\\bar{\\Sigma}^+',1114:'\\Delta^-',
               -1114:'\\bar{\\Delta}^+',2114:'\\Delta^0',
               -2114:'\\bar{\\Delta}^0',3324:'\\Xi^{*0}',
               -3324:'\\bar{\\Xi}^{*0}',2224:'\\Delta^{++}',
               -2224:'\\bar{\\Delta}^{--}',2214:'\\Delta^+',
               -2214:'\\bar{\\Delta}^-',3222:'\\Sigma^+',
               -3222:'\\bar{\\Sigma}^-',3216:'\\Sigma(1775)^0',
               -3216:'\\bar{\\Sigma}(1775)^0',13214:'\\Sigma(1670)^0',
               -13214:'\\bar{\\Sigma}(1670)^0',13212:'\\Sigma(1660)^0',
               -13212:'\\bar{\\Sigma}(1660)^0',13126:'\\Lambda(1830)^0',
               -13126:'\\bar{\\Lambda}(1830)^0',3126:'\\Lambda(1820)^0',
               -3126:'\\bar{\\Lambda}(1820)^0',53122:'\\Lambda(1810)^0',
               -53122:'\\bar{\\Lambda}(1810)^0',43122:'\\Lambda(1810)^0',
               -43122:'\\bar{\\Lambda}(1810)^0',13124:'\\Lambda(1690)^0',
               -13124:'\\bar{\\Lambda}(1690)^0',33122:'\\Lambda(1670)^0',
               -33122:'\\bar{\\Lambda}(1670)^0',23122:'\\Lambda(1600)^0',
               -23122:'\\bar{\\Lambda}(1600)^0',3124:'\\Lambda(1520)^0',
               -3124:'\\bar{\\Lambda}(1520)^0',13122:'\\Lambda(1405)^0',
               -13122:'\\bar{\\Lambda}(1405)^0',3122:'\\Lambda',
               -3122:'\\bar{\\Lambda}',4312:'\\Xi_c^{\'0}',
               -4312:'\\bar{\\Xi}_c^{\'0}',4322:'\\Xi_c^{\'+}',
               -4322:'\\bar{\\Xi}_c^{\'-}',4222:'\\Sigma_c^{++}',
               -4222:'\\bar{\\Sigma}_c^{--}',4232:'\\Xi_c^+',
               -4232:'\\bar{\\Xi_c}^-',4212:'\\Sigma_c^+',
               -4212:'\\bar{\\Sigma}_c^-',4112:'\\Sigma_c^0',
               -4112:'\\bar{\\Sigma}_c^0',84:'X_c',-84:'\\bar{X}_c',
               4132:'\\Xi_c^0',-4132:'\\bar{\\Xi}_c^0',4122:'\\Lambda_c^+',
               -4122:'\\bar{\\Lambda}_c^-',60555:'\\eta_{b2}(2D)',
               40555:'\\eta_{b2}(1D)',100553:'\\Upsilon(2S)',40553:'h_b(2P)',
               10557:'\\Upsilon_3(2D)',50555:'\\Upsilon_2(2D)',
               130553:'\\Upsilon_1(2D)',557:'\\Upsilon_3(1D)',
               30555:'\\Upsilon_2(1D)',120553:'\\chi_{b1}(2P)',
               20555:'\\chi_{b2}(3P)',110553:'\\chi_{b1}(3P)',
               50551:'\\chi_{b0}(3P)',10553:'h_b',10555:'\\chi_{b2}(2P)',
               50553:'\\chi_{b1}(2P)',30551:'\\chi_{b0}(2P)',555:'\\chi_{b2}',
               20553:'\\chi_{b1}(1P)',10551:'\\chi_{b0}(1P)',
               60553:'\\Upsilon(3S)',30553:'\\Upsilon(2S)',553:'\\Upsilon',
               551:'\\eta_b(1S)',40443:'\\psi(3770)',445:'\\chi_{c2}(1P)',
               20443:'\\chi_{c1}(1P)',10441:'\\chi_{c0}(1P)',
               70443:'\\psi(4415)',60443:'\\psi(4160)',50443:'\\psi(4040)',
               30443:'\\psi(2S)',443:'J/\\psi',441:'\\eta_c',
               30113:'\\rho(2S)^0',30213:'\\rho(2S)^+',-30213:'\\rho(2S)^-',
               10333:'h_1(1380)',10223:'h_1(1170)',335:'f\'_2(1525)',
               50221:'f_0(1500)',225:'f_2(1270)',20333:'f_1(1420)',
               20223:'f_1(1285)',10331:'f_0(1710)',10221:'f_0(1370)',
               10211:'a_0(1460)^+',-10211:'a_0(1460)^-',10111:'a_0(1450)^0',
               10113:'b_1^0',10213:'b_1^+',-10213:'b_1^-',115:'a_2^0',
               215:'a_2^+',-215:'a_2^-',20213:'a_1^+',-20213:'a_1^-',
               20113:'a_1^0',333:'\\phi',331:'\\eta\'',223:'\\omega',
               213:'\\rho^+',-213:'\\rho^-',113:'\\rho^0',221:'\\eta',
               30363:'X_{su}',-30363:'\\bar{X}_ss',30353:'X_{su}',
               -30353:'\\bar{X}_{su}',30343:'X_{sd}',-30343:'\\bar{X}_{sd}',
               30323:'K_1(1650)^+',-30323:'K_1(1650)^-',30313:'K_1(1650)^0',
               -30313:'\\bar{K}_1(1650)^0',100323:'K^*(1410)^+',
               -100323:'K^*(1410)^-',100313:'K^*(1410)^0',
               -100313:'\\bar{K}^*(1410)^0',315:'K_2^{*0}',
               -315:'\\bar{K}_2^{*0}',325:'K_2^{*+}',-325:'K_2^{*-}',
               20313:'K_1(1400)^0',-20313:'\\bar{K}_1(1400)^0',
               20323:'K_1(1400)^+',-20323:'K_1(1400)^-',10313:'K_1^0',
               -10313:'\\bar{K}_1^0',10323:'K_1^+',-10323:'K_1^-',
               10311:'K_0^{*0}',-10311:'\\bar{K}_0^{*0}',10321:'K_0^{*+}',
               -10321:'K_0^{*-}',313:'K^{*0}',-313:'\\bar{K}^{*0}',
               323:'K^{*+}',-323:'K^{*-}',311:'K^0',-311:'\\bar{K}^0',
               310:'K_S^0',30413:'D^*(2S)^+',-30413:'D^*(2S)^-',
               30423:'D^*(2S)^0',-30423:'\\bar{D}^*(2S)^0',
               30411:'D(2S)^+',-30411:'D(2S)^-',30421:'D(2S)^0',
               -30421:'\\bar{D}(2S)^0',435:'D_{s2}^{*+}',
               -435:'D_{s2}^{*-}',10433:'D_{s1}(2536)^+',
               -10433:'D_{s1}(2536)^-',20433:'D_{s1}(H)^+',
               -20433:'D_{s1}(H)^-',10431:'D_{s0}^{*+}',-10431:'D_{s0}^{*-}',
               425:'D_2^{*0}',-425:'\\bar{D}_2^{*0}',415:'D_2^{*+}',
               -415:'D_2^{*-}',20423:'D_1(H)^0',-20423:'\\bar{D}_1(H)^0',
               20413:'D_1(H)^+',-20413:'D_1(H)^-',10423:'D_1^0',
               -10423:'\\bar{D}_1^0',10413:'D_1^+',-10413:'D_1^-',
               10411:'D_0^{*+}',-10411:'D_0^{*-}',10421:'D_0^{*0}',
               -10421:'\\bar{D}_0^{*0}',431:'D_s^+',-431:'D_s^-',421:'D^0',
               -421:'\\bar{D}^0',411:'D^+',-411:'D^-',433:'D_s^{*+}',
               -433:'D_s^{*-}',423:'D^{*0}',-423:'\\bar{D}^{*0}',
               413:'D^{*+}',-413:'D^{*-}',531:'B_s^0',-531:'\\bar{B}_s^0',
               533:'B_s^{*0}',-533:'\\bar{B}_s^{*0}',513:'B^{*0}',
               -513:'\\bar{B}^{*0}',523:'B^{*+}',-523:'B^{*-}',511:'B^0',
               -511:'\\bar{B}^0',521:'B^+',-521:'B^-',70553:'\\Upsilon(4S)',
               321:'K^+',-321:'K^-',2212:'p',-2212:'\\bar{p}',
               2112:'n',-2112:'\\bar{n}',81:'X',2103:'(ud)_1',2101:'(ud)_0',
               2203:'(uu)_1',3203:'(su)_1',3201:'(su)_0',21:'g',82:'X',
               -82:'\\bar{X}',130:'K_L^0',-4303:'(\\bar{c}\\bar{s})_1',
               -4301:'(\\bar{c}\\bar{s})_1',20441:'\\eta_c',
               -2103:'(\\bar{u}\\bar{d})_1',4303:'(cs)_1',
               -2101:'(\\bar{u}\\bar{d})_0',
               4301:'(cs)_0',-4103:'(\\bar{c}\\bar{d})_1',
               -2203:'(\\bar{u}\\bar{u})_1',2203:'(uu)_1',
               -4101:'(\\bar{c}\\bar{d})_0',4103:'(cd)_1',
               40213:'\\rho(3S)^+',-40213:'\\rho(3S)^-',4101:'(cd)_0',
               999999:'Pythia'}

if os.access('output.tex',os.F_OK)==1:
    os.remove('output.tex')
outputFile = open( 'output.tex' , 'w' )

def AddDecayEntry( pdgId ):
    if ( latexTable.has_key( pdgId ) ):
        outputFile.write('\\section{')
        outputFile.write('$')
        outputFile.write( latexTable[ pdgId ] )
        outputFile.write('$')
        outputFile.write('}')
        outputFile.write('\\begin{supertabular}{|l|l|}')
        outputFile.write( '\n\n' )
    else:
        print 'Latex symbol does not exist for '
        print pdgId
        print 'Please add it to the source file.'

def CloseDecayEntry( ):
    outputFile.write('\\end{supertabular}')

def AddModeEntry( listParticules ):
    if len(listParticules)>1:
        outputFile.write('$')
        for x in listParticules[1:]:
            if ( latexTable.has_key( x ) ):
                outputFile.write( latexTable[ x ] )
                outputFile.write(' \;\; ')
            else:
                print 'Latex symbol does not exist for '
                print x
                print 'Please add it to the source file.'               
        outputFile.write('$')
        outputFile.write('&')
        outputFile.write(str(listParticules[0]))
        outputFile.write('\\\\')
        outputFile.write('\n')
    else:
        print 'Warning: a particule has an empty decay '
        print 'Check decay file'

def PrepareLatexFile( ):
    outputFile.write('\\documentclass[twocolumn,10pt]{article}\n')
    outputFile.write('\\usepackage{amsmath,amssymb}\n')
    outputFile.write('\\usepackage{times,mathptm}\n')
    outputFile.write('\\usepackage{supertabular}\n')
    outputFile.write('\\begin{document}\n')
    outputFile.write('\\tableofcontents\n')
    outputFile.write('\\pagebreak\n')

def EndLatexFile( ):
    outputFile.write('\\end{document}\n')

def readEvtPdl( ):
    evtPdlPath = 'evt.pdl'
    if os.access ( 'evt.pdl' , os.F_OK ) == 0:
        print 'evt.pdl does not exist in current directory'
        print 'Use '+evtPdlPath+' instead'
        f = open( evtPdlPath , 'r' )
    else:
        f = open( 'evt.pdl' , 'r' )
    line = f.readline()
    while line != '':
        if re.match( "\s*add" , line):
            content = string.split(line)
            pdgTable[ content[3] ] = int(content[4])
        line = f.readline()

def studyLine( line ):
    result = []
    if re.match( "\s*#", line):
        # Comment
        result.append(1)
    elif re.match( "\s*Define", line):
        # Define
        result.append(2)
    elif re.match( "\s*Alias", line):
        # Alias
        content = string.split(line)
        if pdgTable.has_key( content[2] ):
            pdgTable[ content[1] ] = pdgTable[ content[2] ]
        else:
            print 'Error in decayfile: '+content[2]+' is not defined !'
            sys.exit( 0 )
        result.append(3)
    elif re.match( "\s*ChargeConj" , line):
        # ChargeConf
        result.append(4)
    elif re.match( "\s*JetSetPar" , line ) :
        # JetSetPar
        result.append(5)
    elif re.match( "\s*Decay" , line ):
        # Decay
        result.append(6)
        content = string.split(line)
        if pdgTable.has_key( content[1] ):
            result.append( pdgTable[ content[1] ] )
        else:
            print 'Error in decayfile: '+content[1]+ ' is not defined !'
            sys.exit( 0 )
    elif re.match( "\s*Enddecay" , line ):
        # Decay
        result.append(7)
    elif re.match( "\s*[0-9\.]+\s+\D+" , line ):
        # Decay Mode
        result.append(8)
        content = string.split(line)
        result.append( float( content[0] ) )
        i = 1
        while (content[i].rstrip(';') in decayModels) == 0:
            if pdgTable.has_key( content[i] ):
                result.append( pdgTable[ content[i] ] )
            else:
                print 'Error in decay file: ' +content[i]+ ' is not defined !'
                sys.exit( 0 )
            i = i + 1
        if pdgTable.has_key( content[i].rstrip(';') ):
            result.append( pdgTable[ content[i].rstrip(';') ] )
    return result

def readDecFile(file):
    f = open( file , 'r' )
    line = f.readline()
    while line != '':
        typeLine = studyLine( line )
        if len(typeLine) > 0:
            if typeLine[0] == 6:
                AddDecayEntry( typeLine[1] )
                line = f.readline()
                while line != '':
                    typeLine = studyLine( line )
                    if len(typeLine) > 0:
                        if typeLine[0] == 7:
                            CloseDecayEntry()
                            break
                        elif typeLine[0] == 8:
                            AddModeEntry(typeLine[1:])
                    line = f.readline()
                    if line=='':
                        print 'Decay wihout Enddecay !'
                        sys.exit( 0 )
        line = f.readline()
    f.close()

print 'This script is known to work with python 2.2'
print 'At CERN, run it with python2.2'
if len ( sys.argv ) != 2:
    print 'Usage : displayEvtTable [DECAY FILE]'
else:
    decayFileName = sys.argv[1]
    print 'Read decay table from ' + decayFileName
    if os.access ( decayFileName , os.F_OK ) == 0:
        print decayFileName + ' does not exist !'
        sys.exit( 0 )
    readEvtPdl( )
    PrepareLatexFile( )
    readDecFile( decayFileName )
    EndLatexFile( ) 
    outputFile.close()
    
