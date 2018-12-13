#! /usr/bin/env python
## Author: Luca Pescatore, modified by Matthieu Marinangeli
## Mail: pluca@cern.ch
## Description: script to submit jobs (mostly done for lxplus but for local submissions works anywhere)
## N.B.: Needs an environment variable "JOBDIR" which is the location to put jobs outputs

import os, sys, shutil
from string import *
import re
from argparse import ArgumentParser
import subprocess as sub
import random
from datetime import datetime
import time
import getpass
import warnings

def PrepareLxplusJob(**kwargs):
    
    user = getpass.getuser()
    
    time     = kwargs.get("time", 7) #Maximum time of the job in hours (Slurm).
    subdir   = kwargs.get("subdir", "")
    jobname  = kwargs.get("jobname", "")
    dirname  = kwargs.get("dirname" )
    queue    = kwargs.get("queue", "1nd") #Choose bach queue (default 1nd) (lxplus) 
    mail     = kwargs.get("mail", False) #When job finished sends a mail to USER@cern.ch (lxplus)
    loginprod = kwargs.get("loginprod", True)
    clean    = kwargs.get("clean", True)
    
    if mail: mail = "-u "+user+"@cern.ch"
    else: mail = ""

    #prepare lxplus batch job submission
        
    if not loginprod:
        logdir = os.getenv("LOG_SIMOUTPUT")
        
        if logdir is None:
            logdirname = "/afs/cern.ch/work/{0}/{1}/{2}/{3}".format( user[0], user, subdir, jobname)
        else:
            logdirname = "{0}/{1}/{2}".format( logdir, subdir, jobname)
            
        if os.path.exists(logdirname) and clean :
            shutil.rmtree(logdirname, ignore_errors = True)
        os.makedirs(logdirname) 
        
    else:
        logdirname = dirname
        
    command = "bsub -R 'pool>30000' -o {logdir}/out -e {logdir}/err \
            -q {queue} {mail} -J {jname} < {dir}/run.sh".format(
                    dir = dirname, queue = queue,
                    mail = mail, jname = subdir + jobname,
                    logdir = logdirname )
            
    return command
    
def SendCommand(command):
        
    if sys.version_info[0] > 2:
        process = sub.Popen(command, shell = True, stdout=sub.PIPE, stderr=sub.PIPE, encoding='utf8')
    else:
        process = sub.Popen(command, shell = True, stdout=sub.PIPE, stderr=sub.PIPE)
        
    time.sleep(0.03)
    out, err = process.communicate()
            
    return out
    
def PrepareSlurmJob(**kwargs):
    
    #prepare slurm batch job submission
    
    subdir    = kwargs.get("subdir", "")
    jobname   = kwargs.get("jobname", "")        
    cpumemory = kwargs.get("cpumemory", 2800)        #Memory per cpu (Slurm).
    totmemory = kwargs.get("totmemory", 4000)
    time      = kwargs.get("time", 20 )         #Maximum time of the job in hours (Slurm).
    exclude   = kwargs.get("nfreenodes", 0)       #Number of nodes to exclude (Slurm).
    nodestoexclude  = kwargs.get("nodestoexclude", [])   #Nodes to exclude (Slurm).
    dirname   = kwargs.get("dirname")

    def GetSlurmNodes():
        
        cmd = sub.Popen(['sinfo','-N'], stdout=sub.PIPE)
        cmd_out, _ = cmd.communicate()    
        output = cmd_out.split("\n")
        output.remove(output[0])
        
        list_nodes = []
        for o in output:
            if "batch" in o:
                list_nodes.append( o.split(" ")[0] )
                
        return list_nodes
        
    oldrun = open(dirname+"/run.sh")
    oldrunstr = oldrun.read()
    oldrun.close()

    fo = open(dirname+"/run.sh","w")
    fo.write("#!/bin/bash -fx\n")                       
    fo.write("#SBATCH -o " + dirname + "/out\n")
    fo.write("#SBATCH -e " + dirname + "/err\n")
    fo.write("#SBATCH -J " + subdir + jobname + "\n")
    fo.write("#SBATCH --mem {0}".format(totmemory) + "\n")
    fo.write("#SBATCH --mem-per-cpu {0}".format(cpumemory) + "\n")
    fo.write("#SBATCH -n 1\n")
    fo.write("#SBATCH -p batch\n")
    fo.write("#SBATCH -t {0}:00:00\n".format(time))
    if exclude != 0 or len(nodestoexclude) > 0:
        
        now = datetime.now()
        random.seed(now.day)
        
        nodes = GetSlurmNodes()
        random.shuffle(nodes)
        
        n2exclude = int(exclude) + len(nodestoexclude)
        
        #### check if nodes exit
        exists = all(n in nodes for n in nodestoexclude)
        
        if not exists:
            _nodestoexclude = []
            for n in nodestoexclude:
                if not n in nodes:
                    warnings.warn( red(" WARNING: node {0} does not exist. \
                                It will be removed!".format(n)), stacklevel = 2 )
                else:
                    _nodestoexclude.append(n)
            nodestoexclude = _nodestoexclude
            
        for n in nodestoexclude:
            nodes.remove(n)

        nodes = nodes[0:(n2exclude - len(nodestoexclude))]
        nodes += nodestoexclude
        
        nodes2exclude = ""
        for n in nodes:
            if n == nodes[-1]: nodes2exclude += n
            else: nodes2exclude += n +","
                
        fo.write("#SBATCH --exclude={0}\n\n\n".format(nodes2exclude))
    
    fo.write(oldrunstr)
    fo.close()
    
    command = "sbatch "+dirname+"/run.sh"
    return command

def main( **kwargs ):
    
    jobdir = os.getenv("SIMOUTPUT")
    
    if jobdir is None :
        jobdir = os.getenv("HOME")+"/jobs"
        os.makedirs(jobdir)

    subdir   = kwargs.get("subdir", "")       #Folder of the job, notice that the job is created anyway in a folder called as the jobname, so this is intended to group jobs.
    run      = kwargs.get("run", -1)          #Add run number.
    basedir  = kwargs.get("basedir", jobdir)  #This option bypasses the JOBDIR environment variable and creates the job's folder in the specified folder.
    jobname  = kwargs.get("jobname", "")      #Give a name to the job. The job will be also created in a folder with its name (default is the executable name).
    clean    = kwargs.get("clean", True)      #If the job folder already exists by default it cleans it up. This option bypasses the cleaning up.
    unique   = kwargs.get("unique", True)     #Copy the executable only once in the top folder (and not in each job folders).
    infiles  = kwargs.get("infiles", [])      #Files to copy over.
    command  = kwargs.get("command", "")      #Command to launch.
    slurm    = kwargs.get("slurm", False)
    lsf      = kwargs.get("lsf", False)

    exe, execname = None, None
    commands = command.split(' ')
    
    if(len(commands) < 1) : print("Not enough arguments")
    elif "." in commands[0] : 
        execname = commands[0].replace('./','')
        args = commands[1:]
    elif "lb-run" in commands[0] :
        exe      = "{0} {1} {2}".format(commands[0],commands[1],commands[2])
        execname = commands[3]
        args = commands[4:]
    elif len(commands) > 1 : 
        execname = commands[1]
        exe      = commands[0]
        args = commands[2:]
        
        if not "." in execname:
            execname  = ""
            args = commands[1:]
            
    else : sys.exit()
    if( jobname == "" ) :
        jobname = re.sub(r'\..*',"", execname.replace('./',''))

    ########################################################################################
    ## Make the needed folders and copy the executable and everything else needed in them
    ########################################################################################
    
    try:
    
        subdirname = basedir
        if subdir != "" :
            subdirname += "/"+subdir
        dirname = subdirname+"/"+jobname

        if run > -1 :
            dirname += "_"+str(run)

        if os.path.exists(dirname) and clean :
            shutil.rmtree(dirname, ignore_errors = True)
        os.makedirs(dirname)
        
        kwargs['dirname'] = dirname

        if( unique ) : copyto = subdirname
        else : copyto = dirname
        
        if not execname == "":
            shutil.copyfile(execname, "{0}/{1}".format(copyto, os.path.basename(execname)))
        if '/'  in execname :
            execname = execname.split("/")[-1]
        
        for arg in infiles :
            shutil.copyfile(arg, "{0}/{1}".format(dirname, os.path.basename(arg)))
                
        ########################################################################################
        ## Create the run.sh file containing the information about how the executable is run
        ########################################################################################

        runfile = open(dirname+"/run.sh","w")
        runfile.write( "cd " + dirname + "\n")

        if exe is None:
            runfile.write("chmod 755 " + copyto + "/" +execname +'\n')

        if  execname == "":
            pathexec = ""
        else:
            pathexec = copyto+"/"+execname
            
        if exe is None:
            runfile.write( '{dir} {args}'.format(dir=pathexec,args=' '.join(args)) + "\n")
        else :
            runfile.write( '{exe} {dir} {args}'.format(exe=exe,dir=pathexec,args=' '.join(args)) + "\n")
            
        runfile.close()
        sub.call(['chmod', '775', dirname + "/run.sh"])
        
        ########################################################################################
        ## Run executable in local, interactive or batch mode and send
        ########################################################################################
        
        if( subdir != "" ) :
            subdir = (re.sub("^.*/","",subdir)+"_")
                
        if "lxplus" in os.getenv("HOSTNAME") and lsf:  ## Batch for lxplus
            command = PrepareLxplusJob( **kwargs )
            out = SendCommand( command )
            try:
                ID = int( out.split(" ")[1].replace(">","").replace("<","") )
                print( "Submitted batch job {0}".format(ID) )
                return ID
            except IndexError:
                return None
            
        elif slurm:
            command = PrepareSlurmJob( **kwargs )
            out = SendCommand( command )
            ID = int( out.split(" ")[-1] )
            print( "Submitted batch job {0}".format(ID) )
            return ID
        
        else :
            print("Can run in batch mode only on lxplus or on a slurm batch system.")
     
    
    except IOError:
        return None
    
    
          
    
        
        



