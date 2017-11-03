# Author: Marc-Olivier Bettler
# Version: 1.0
# Comment: You have to run the script in the dkfiles directory

"""Give a list of decfiles"""

import sys, string
from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile
from glob import glob
import os
from datetime import date
from optparse import OptionParser
import shutil
#from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=4)


DEBUG =  False #True#
listOfDic = []
list_evt = []


def PrintOutDuplicate( evttype, listOfDic ):
    #find in listOfDic the occurence of evtype

    print_order = [  ['Decfile', '\n']
                ,['EventType', '\n']
                ,['Descriptor', '\n']
                ,['NickName', '\n']
                ,['PhysicsWG', '\n']
                ,['Tested', '\n']
                ,['Responsible', '\n']
                ,['Email', '\n']
                ,['Date', '\n']
                ]

    duplicated = []
    for dic in listOfDic:
        if dic['EventType']['Content'] == evttype:
            duplicated.append( dic )

    
    for dic in duplicated:
        new_content = ''
        for item in print_order:
            if dic[item[0]]['Content'] == None:
                continue
            new_content += dic[item[0]]['New_key']
            new_content += ': '
            new_content += dic[item[0]]['Content']
            new_content += item[1]
        print new_content
        #print '++++'


list_decfiles = glob('*dec')

for decfile in list_decfiles:
    f = open(decfile)
    content = f.read()

    # optional fields are initialised as None
    d     = { 'EventType': {'New_key': 'EventType'  ,'Content':'', 'Old_key':'EventType' }
         ,'Descriptor':    {'New_key': 'Descriptor' ,'Content':'', 'Old_key':'Descriptor'}
         ,'NickName':      {'New_key': 'NickName'   ,'Content':'', 'Old_key':'NickName'  }
         ,'PhysicsWG':     {'New_key': 'PhysicsWG'  ,'Content': '', 'Old_key': 'PhysicsWG'                  }
         ,'Tested':        {'New_key': 'Tested'     ,'Content': '', 'Old_key':'Tested'   }
         ,'Responsible':   {'New_key': 'Responsible','Content': '', 'Old_key':'Responsible'       }
         ,'Email':         {'New_key': 'Email'      ,'Content': '', 'Old_key': 'Email'                       }
         ,'Date':          {'New_key': 'Date'       ,'Content': '', 'Old_key':'Date'     }
         ,'Decfile':       {'New_key': 'Decfile'    ,'Content': decfile}
         }
   
    
    for field in d.keys():
        if 'Old_key' in d[field]:
            #if DEBUG:  print field, content.find(d[field]['Old_key'])
            if content.find(d[field]['Old_key']) != -1:
                beg = content.find(d[field]['Old_key'])+len( d[field]['Old_key'] )+1
                end = content.find('\n', beg)
                d[field]['Content'] = content[beg:end]
            else:
                print 'Could not find field ', d[field]['Old_key'], ' in file ', decfile

    #if DEBUG:
        #pp.pprint(d)
        #print content[deepest:]
        #import code; code.interact(local=locals())

    f.close()
    d['EventType']['Content'] = str(int( d['EventType']['Content'] ))
    listOfDic.append( d )
    list_evt.append( d['EventType']['Content'] )


#analyse
if DEBUG: import code; code.interact(local=locals())

print '\n\n', len(list_evt)- len(set(list_evt)), 'duplicated decfiles\n'
for evttype in set(list_evt):
    if list_evt.count( evttype ) != 1:
        
        print '----  Found ', list_evt.count( evttype ), ' dec files with evttype ', evttype, '\n'
        PrintOutDuplicate( evttype, listOfDic )
        print '---------------------------\n\n'

## for d in listOfDic:

##     new_content = ''
##     for item in print_order:
##         if d[item[0]]['Content'] == None:
##             continue
##         new_content += '# '
##         new_content += d[item[0]]['New_key']
##         new_content += ': '
##         new_content += d[item[0]]['Content']
##         new_content += item[1]
##     new_content += d['REST']['Content']

##     if DEBUG:
##         pp.pprint('new content:\n')
##         print new_content  
##         import code; code.interact(local=locals())

##     suffix = '_'+date.today().strftime('%Y%m%d')
##     new_file = open(decfile_path+suffix, 'w')
##     new_file.write(new_content)   
        
