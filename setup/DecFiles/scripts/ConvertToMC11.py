
"""Give a list of decfiles"""

import sys, string
from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile
from glob import glob
import os
from datetime import date
from optparse import OptionParser
import shutil
import pprint
pp = pprint.PrettyPrinter(indent=4)

def parse_options():
    
    opt = OptionParser("usage: %prog [options] <DecFiles>\n\n       <DecFiles> : list of ProdID(s)Decfile (s), colon separated (:), with no blank spaces.")

    opt.add_option("-w", "--working-group",
                   action="store", dest="WG", type="string", 
                   metavar='<WORKING_GROUP>',
                   default='RD',
                   help="Physics Working Group [default : RD]")

    opt.add_option("-d",
                   action="store_true", dest="debug",
                   default=False,
                   help="verbose for debugging purpose")

##     opt.add_option("-n", "--number-of-logs",
##                    action="store", type="int", dest="nb_logs",
##                    default=300,
##                    metavar='<NB_LOGS>',
##                    help="number of logs to download [default : %default]")

##     opt.add_option("--delta-size",
##                    action="store", type="float", dest="delta",
##                    default=0.07,
##                    metavar='<DELTA>',
##                    help="log files smaller by <DELTA> from largest file of sample will be deleted [default : %default]")
    
    opt.add_option("--usage",
                   action="store_true", dest="print_usage",
                   default=False,
                   help="show this help message and exit")

    (options, args) = opt.parse_args()
    if options.print_usage :
        opt.print_help()
        exit()
    if len(args) != 1:
        opt.error("Incorrect number of arguments, should be a colon-separated list of ProdID(s).")

    # treating options
    global base_path, WG_OPT, DEBUG 
    WG_OPT    = options.WG
    DEBUG     = options.debug
    base_path = os.path.abspath(os.curdir) #base_path = options.base_path
    if not os.path.isabs( base_path ) :
        base_path = os.path.join( os.path.abspath(os.curdir), base_path )

    # treating args
    global list_decfiles
    list_decfiles = args[0].replace(' ',':').split(':')
    #import code; code.interact(local=locals())


parse_options()

print base_path , list_decfiles

print_order = [  ['EventType', '\n#\n']
                ,['Descriptor', '\n#\n']
                ,['NickName', '\n#\n']
                ,['Cuts', '\n#\n']
                ,['FullEventCuts', '\n']
                ,['Sample', '\n']
                ,['ExtraOptions', '\n']
                ,['Documentation', '\n# EndDocumentation\n#\n']
                ,['PhysicsWG', '\n']
                ,['Tested', '\n']
                ,['Responsible', '\n']
                ,['Email', '\n']
                ,['Date', '\n']
                ]

for decfile in list_decfiles:
    decfile_path = os.path.join( base_path, decfile )
    if not os.path.exists(decfile_path):
        print 'Inexising decfile, ', decfile_path
        continue
    f = open(decfile_path)
    content = f.read()

    # optional fields are initialised as None
    d     = { 'EventType':     {'New_key': 'EventType'     ,'Content':'', 'Old_key':'EventType' }
         ,'Descriptor':    {'New_key': 'Descriptor'    ,'Content':'', 'Old_key':'Descriptor'}
         ,'NickName':      {'New_key': 'NickName'      ,'Content':'', 'Old_key':'NickName'  }
         ,'Cuts':          {'New_key': 'Cuts'          ,'Content':'LHCbAcceptance','Old_key':'Cuts'}
         ,'Documentation': {'New_key': 'Documentation' ,'Content':'', 'Old_key':'Physics'   }
         ,'PhysicsWG':     {'New_key': 'PhysicsWG'     ,'Content': WG_OPT                   }
         ,'Tested':        {'New_key': 'Tested'        ,'Content': '', 'Old_key':'Tested'   }
         ,'Responsible':   {'New_key': 'Responsible'   ,'Content': '', 'Old_key':'By'       }
         ,'Email':         {'New_key': 'Email'         ,'Content': ''                       }
         ,'Date':          {'New_key': 'Date'          ,'Content': '', 'Old_key':'Date'     }
         ,'FullEventCuts': {'New_key': 'FullEventCuts' ,'Content':None,'Old_key':'FullEventCuts'}
         ,'Sample':        {'New_key': 'Sample'        ,'Content':None                      }
         ,'ExtraOptions':  {'New_key': 'ExtraOptions'  ,'Content':None,'Old_key':'ExtraOptions' }
         ,'REST':          {                            'Content': ''                       }
         }
   
    deepest = 0 #measures the end of the header
    for field in d.keys():
        if 'Old_key' in d[field]:
            if DEBUG:  print field, content.find(d[field]['Old_key'])
            if content.find(d[field]['Old_key']) != -1:
                if field == 'Documentation' : #in case of the Documentation multiple lines areaccepted, difficult to read from old files
                    if DEBUG: print '-------------------------'
                    beg = content.find(d[field]['Old_key'])+len( d[field]['Old_key'] )+1
                    closest = 9999
                    for other_field in d.keys():
                        if other_field == 'Documentation'  : continue
                        if 'Old_key' not in d[other_field] : continue
                        if content.find(d[other_field]['Old_key'], beg) > beg :
                            closest = min( closest, content.find(d[other_field]['Old_key'], beg) )
                        
                        if DEBUG:
                            print other_field, closest
                            #import code; code.interact(local=locals())
                    end = closest
                    d[field]['Content'] = content[beg:end]
                    if end > deepest:
                        deepest = end
                    if DEBUG: print '-------------------------'
                else :
                    beg = content.find(d[field]['Old_key'])+len( d[field]['Old_key'] )+1
                    end = content.find('\n', beg)
                    d[field]['Content'] = content[beg:end]
                    if end > deepest:
                        deepest = end
            else:
                print 'Could not find field ', d[field]['Old_key'], ' in file ', decfile

    d['REST']['Content'] = content[deepest:].strip('\n')+'\n'
    
    if DEBUG:
        pp.pprint(d)
        print content[deepest:]
        import code; code.interact(local=locals())

    f.close()

    new_content = ''
    for item in print_order:
        if d[item[0]]['Content'] == None:
            continue
        new_content += '# '
        new_content += d[item[0]]['New_key']
        new_content += ': '
        new_content += d[item[0]]['Content']
        new_content += item[1]
    new_content += d['REST']['Content']

    if DEBUG:
        pp.pprint('new content:\n')
        print new_content  
        import code; code.interact(local=locals())

    suffix = '_'+date.today().strftime('%Y%m%d')
    new_file = open(decfile_path+suffix, 'w')
    new_file.write(new_content)   
        
