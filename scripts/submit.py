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

## Rutines

if __name__ == "__main__" :

    jobdir = os.getenv("JOBDIR")
    
    if jobdir is None :
        jobdir = os.getenv("HOME")+"/jobs"
        os.system("mkdir -p "+jobdir)
        
    parser = ArgumentParser()
    parser.add_argument("-d", default="", dest="subdir", 
        help="Folder of the job, notice that the job is created anyway in a folder called as the jobname, so this is intended to group jobs")
    parser.add_argument("-r", default=-1, dest="run", help="Add run number")
    parser.add_argument("-D", default=jobdir, dest="basedir",
        help="This option bypasses the JOBDIR environment variable and creates the job's folder in the specified folder")
    parser.add_argument("-n", default="", dest="jobname", 
        help="Give a name to the job. The job will be also created in a folder with its name (default is the executable name)")
    parser.add_argument("--bash", dest="shell", default = "", action="store_const", const = "#!/usr/bin/env bash",
        help="Initialize a new bash shell before launching" )
    parser.add_argument("--tcsh", dest="shell", default = "", action="store_const", const = "#!/usr/bin/env tcsh",
        help="Initialize a new tcsh shell before launching" )
    parser.add_argument("-q", dest="queue", default = "8nh", help="Choose bach queue (default 8nh)" )
    parser.add_argument("-s", dest="setup", default = "", help="Add a setup line to the launching script" )
    parser.add_argument("-se", dest="setup_end", default = "", help="Add a setup line at the end of the launching script" )
    parser.add_argument("--noClean", dest="clean", action="store_false",
        help="If the job folder already exists by default it cleans it up. This option bypasses the cleaning up" )
    parser.add_argument("--interactive", dest="interactive", action="store_true",
        help="Submits on lxplus without using the batch system" )
    parser.add_argument("--uexe", dest="unique", action="store_true",
        help="Copy the executable only once in the top folder (and not in each job folders)" )
    parser.add_argument("--local", dest="local",  action="store_true",
        help="Launch the jobs locally (and not in the batch system)" )
    parser.add_argument("--noscript", dest="noscript",  action="store_true",
        help="Does not put the automatic ./ in front of the executable" )
    parser.add_argument("-m", dest="mail", default = "", action="store_const", const = "-u "+os.environ["USER"]+"@cern.ch",
        help="When job finished sends a mail to USER@cern.ch" )
    parser.add_argument("-cpu", default=3000, dest="m_cpu", 
        help="Memory per cpu.")
    parser.add_argument("-time", default=20, dest="m_time", 
        help="Maximum time of the job in hours.")
    parser.add_argument("-exclude", default=0, dest="m_exclude", 
        help="Number of nodes to exclude.")
    parser.add_argument("-in", dest="infiles", default = "", help="Files to copy over")
    parser.add_argument("command", help="Command to launch")
    opts = parser.parse_args()
    
    now = datetime.now()
    random.seed(now.day * 100 + now.hour)
    exe, execname = None, None
    commands = opts.command.split(' ')

    if(len(commands) < 1) : print("Not enough arguments")
    elif "." in commands[0] : 
        execname = commands[0].replace('./','')
        args = commands[1:]
    elif "lb-run" in commands[0]:
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
    if(opts.jobname == "") :
        jobname = re.sub(r'\..*',"", execname.replace('./',''))
   
    ## Make the needed folders and copy the executable and everything else needed in them
    
    subdirname = opts.basedir
    if opts.subdir != "" :
        subdirname += "/"+opts.subdir
    dirname = subdirname+"/"+opts.jobname

    if opts.run > -1 :
        dirname += "_"+str(opts.run)

    if os.path.exists(dirname) and opts.clean :
        os.system("rm -fr " + dirname+"/*")
    os.system("mkdir -p " + dirname)

    if(opts.unique) : copyto = subdirname
    else : copyto = dirname
    
    if not execname == "":
        os.system("cp " + execname + " " + copyto )
    if '/'  in execname :
        execname = execname.split("/")[-1]
    
    for arg in opts.infiles.split() :
        os.system("cp " + arg + " " + copyto )
        if opts.unique :
            os.system("ln -s {f1} {f2}".format(f1=copyto+'/'+arg,f2=dirname+'/'+arg))
    
    ## Create the run.sh file containing the information about how the executable is run

    os.system( "cd " + dirname )
    runfile = open(dirname+"/run.sh","w")
    if opts.shell != "" :                   ### Settings    
        runfile.write(opts.shell + "\n")
    runfile.write( "cd " + dirname + "\n")
    if opts.setup != "" :
        runfile.write(opts.setup + "\n")
    if exe is None and not opts.noscript:   ### Ensure executable
        runfile.write("chmod 755 " + copyto + "/" +execname +'\n')

    if  execname == "":
        pathexec = ""
    else:
        pathexec = copyto+"/"+execname
        
    if exe is None:
        runfile.write( '{dir} {args}'.format(dir=pathexec,args=' '.join(args)) + "\n")
    else :
        runfile.write( '{exe} {dir} {args}'.format(exe=exe,dir=pathexec,args=' '.join(args)) + "\n")
        
    if opts.setup_end != "" :
        runfile.write(opts.setup_end + "\n")

    if opts.local or opts.interactive :     ### Output
        runfile.write( " >& " + dirname + "/out " )
    runfile.close()
    os.system( "chmod 755 " + dirname + "/run.sh" )

    ## Run executable in local, interactive or batch mode
    
    if(opts.subdir != "") :
        opts.subdir=(re.sub("^.*/","",opts.subdir)+"_")
    
    if opts.local :                           ## Local
        print("Running local")
        os.system( "cd " + dirname )
        os.system( dirname + "/run.sh &" )

    elif "lxplus" in os.getenv("HOSTNAME") :  ## Batch for lxplus
        if opts.interactive :
            launch_interactive(dirname)
        else :
            cmd = "bsub -R 'pool>30000' -o {dir}/out -e {dir}/err \
                    -q {queue} {mail} -J {jname} < {dir}/run.sh".format(
                        dir=dirname,queue=opts.queue,
                        mail=opts.mail,jname=opts.subdir+opts.jobname)
            os.system(cmd)

    elif 'lphe' in os.getenv("HOSTNAME") :    ## Batch for EPFL
        cmd = "sbatch "+dirname+"/run.sh"

        oldrun = open(dirname+"/run.sh")
        oldrunstr = oldrun.read()
        oldrun.close()

        fo = open(dirname+"/run.sh","w")
        fo.write("#!/bin/bash -fx\n")                       
        fo.write("#SBATCH -o "+dirname+"/out\n")
        fo.write("#SBATCH -e "+dirname+"/err\n")
        fo.write("#SBATCH -J "+opts.subdir+opts.jobname+"\n")
        fo.write("#SBATCH --mem-per-cpu "+str(opts.m_cpu)+"\n")
        #fo.write("#SBATCH -N 1\n")
        fo.write("#SBATCH -n 1\n")
        fo.write("#SBATCH -p batch\n")
        fo.write("#SBATCH -t {0}:00:00\n\n\n".format(opts.m_time))
        if opts.m_exclude != 0:
            
            nodes  = ["lphe0{0}".format(i) for i in range(1,10)]
            nodes += ["lphe{0}".format(i) for i in range(10,21)]
            random.shuffle(nodes)
            nodes = nodes[0:int(opts.m_exclude)]
            
            nodes2exclude = ""
            for n in nodes:
                if n == nodes[-1]:
                    nodes2exclude += n
                else:
                    nodes2exclude += n +","
        
            
            fo.write("#SBATCH --exclude={0}\n".format(nodes2exclude))
        
        fo.write(oldrunstr)
        fo.close()
        os.system(cmd)

    else :
        print("Can run in batch mode only on lxplus or the EPFL cluster. Go there or run with '--local'")


