#! /usr/bin/env python
## Author: Luca Pescatore, modified by Matthieu Marinangeli
## Mail: pluca@cern.ch
## Description: script to submit jobs (mostly done for lxplus but for local submissions works anywhere)
## N.B.: Needs an environment variable "JOBDIR" which is the location to put jobs outputs

import os, sys
from string import *
import re
from argparse import ArgumentParser
import subprocess as sub
import random
from datetime import datetime

def PrepareLxplusJob( **kwargs ):
    
    cpu      = kwargs.get( "cpu", 4000 )        #Memory per cpu (Slurm).
    time     = kwargs.get( "time", 20 )         #Maximum time of the job in hours (Slurm).
    subdir   = kwargs.get( "subdir", "" )
    jobname  = kwargs.get( "jobname", "" )
    dirname  = kwargs.get( "dirname" )
    queue    = kwargs.get( "queue", "1nd") #Choose bach queue (default 1nd) (lxplus) 
    mail     = kwargs.get( "mail", False) #When job finished sends a mail to USER@cern.ch (lxplus)
    
    if mail: mail = "-u "+os.environ["USER"]+"@cern.ch"
    else: mail = ""
        
    #prepare lxplus batch job submission
    
    command = "bsub -R 'pool>30000' -o {dir}/out -e {dir}/err \
            -q {queue} {mail} -J {jname} < {dir}/run.sh -M {cpu}".format(
                    dir = dirname, queue = queue,
                    mail = mail, jname = subdir + jobname,
                    cpu  = cpu )
    
    return command

def PrepareSlurmJob( **kwargs ):
    
    #prepare slurm batch job submission
    
    subdir   = kwargs.get( "subdir", "" )
    jobname  = kwargs.get( "jobname", "" )
    cpu      = kwargs.get( "cpu", 4000 )        #Memory per cpu (Slurm).
    time     = kwargs.get( "time", 20 )         #Maximum time of the job in hours (Slurm).
    exclude  = kwargs.get( "nfreenodes", 0 )       #Number of nodes to exclude (Slurm).
    dirname  = kwargs.get( "dirname" )

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
    fo.write("#SBATCH --mem-per-cpu {0}".format( cpu ) +"\n")
    fo.write("#SBATCH -n 1\n")
    fo.write("#SBATCH -p batch\n")
    fo.write("#SBATCH -t {0}:00:00\n".format( time ))
    if exclude != 0:
        
        now = datetime.now()
        random.seed(now.day)
        
        nodes = GetSlurmNodes()
        random.shuffle(nodes)
        nodes = nodes[0:int(exclude)]
        
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
    
    jobdir = os.getenv("JOBDIR")
    
    if jobdir is None :
        jobdir = os.getenv("HOME")+"/jobs"
        os.system("mkdir -p "+jobdir)

    subdir   = kwargs.get( "subdir", "" )       #Folder of the job, notice that the job is created anyway in a folder called as the jobname, so this is intended to group jobs.
    run      = kwargs.get( "run", -1 )          #Add run number.
    basedir  = kwargs.get( "basedir", jobdir )  #This option bypasses the JOBDIR environment variable and creates the job's folder in the specified folder.
    jobname  = kwargs.get( "jobname", "" )      #Give a name to the job. The job will be also created in a folder with its name (default is the executable name).
    clean    = kwargs.get( "clean", True )      #If the job folder already exists by default it cleans it up. This option bypasses the cleaning up.
    unique   = kwargs.get( "unique", True )    #Copy the executable only once in the top folder (and not in each job folders).
    infiles  = kwargs.get( "infiles", [] )      #Files to copy over.
    command  = kwargs.get( "command", "" )      #Command to launch.
    slurm    = kwargs.get( "slurm", False )
    lsf      = kwargs.get( "lsf", False )
        
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
    
    subdirname = basedir
    if subdir != "" :
        subdirname += "/"+subdir
    dirname = subdirname+"/"+jobname

    if run > -1 :
        dirname += "_"+str(run)

    if os.path.exists(dirname) and clean :
        os.system("rm -rf " + dirname+"/*")
    os.system("mkdir -p " + dirname)
    
    kwargs['dirname'] = dirname

    if( unique ) : copyto = subdirname
    else : copyto = dirname
    
    if not execname == "":
        os.system("cp " + execname + " " + copyto )
    if '/'  in execname :
        execname = execname.split("/")[-1]
    
    for arg in infiles :
        os.system("cp " + arg + " " + dirname )
            
    ########################################################################################
    ## Create the run.sh file containing the information about how the executable is run
    ########################################################################################

    os.system( "cd " + dirname )
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
    os.system( "chmod 755 " + dirname + "/run.sh" )
    
    ########################################################################################
    ## Run executable in local, interactive or batch mode and send
    ########################################################################################
    
    if( subdir != "" ) :
        subdir = (re.sub("^.*/","",subdir)+"_")
            
    if "lxplus" in os.getenv("HOSTNAME") and lsf:  ## Batch for lxplus
        command = PrepareLxplusJob( **kwargs )
        process = sub.Popen( command, shell = True, stdout=sub.PIPE, stderr=sub.PIPE )
        out, err = process.communicate()
        ID = int( out.split(" ")[1].replace(">","").replace("<","") )
        print( "Submitted batch job {0}".format(ID) )
        return ID
        
    elif slurm:
        command = PrepareSlurmJob( **kwargs )
        process = sub.Popen( command, shell = True, stdout=sub.PIPE, stderr=sub.PIPE )
        out, err = process.communicate()
        ID = int( out.split(" ")[-1] )
        print( "Submitted batch job {0}".format(ID) )
        return ID
     
    else :
        print("Can run in batch mode only on lxplus or on a slurm batch system.")
     
    ########################################################################################
    ## Execution of the job sending and take id
    ########################################################################################
          
    
        
        



