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

now = datetime.now()
random.seed(now.day * 100 + now.hour)

#### Routines for intercative lxplus submission ####

def getRdmNode() :

    node = 'lxplus{0:04d}'.format(random.randint(1,500))
    out = sub.check_output("ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no %s 'ls $HOME/.tcshrc' 2> /dev/null | wc -l" % node, shell = True)
    return [node, out]

def getAliveNode() :
    
    node, out = getRdmNode()
    while int(out) != 1 :
        node, out = getRdmNode()
    return [node, out]

def LaunchInteractive( Dirname ):

    print("Searching for an alive node...")
    node, out = getAliveNode()
    print("Submitting to ", node)
    
    command  = 'ssh -o StrictHostKeyChecking=no %s "cd ' % node + dirname  + '; chmod +x run.sh ; ./run.sh" &'
    command += ' ; echo "Start: {0}"'.format(datetime.now()) 

    return command 
    
def PrepareLxplusJob( Options, Dirname ):
    
    #prepare lxplus batch job submission
    
    command = "bsub -R 'pool>30000' -o {dir}/out -e {dir}/err \
            -q {queue} {mail} -J {jname} < {dir}/run.sh".format(
                dir=Dirname,queue=Options.queue,
                mail=Options.mail,jname=Options.subdir+Options.jobname)
    
    return command

    
def IsSlurm():
    
    # Check if there is a slurm batch system
    
    try:
        sub.Popen(['squeue'], stdout=sub.PIPE)
    except OSError:
        return False
    else:
        return True
        
def PrepareSlurmJob( Options, Dirname ):
    
    #prepare slurm batch job submission
    
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
    fo.write("#SBATCH -o " + Dirname + "/out\n")
    fo.write("#SBATCH -e " + Dirname + "/err\n")
    fo.write("#SBATCH -J " + Options.subdir + Options.jobname + "\n")
    fo.write("#SBATCH --mem-per-cpu "+str(Options.m_cpu)+"\n")
    fo.write("#SBATCH -n 1\n")
    fo.write("#SBATCH -p batch\n")
    fo.write("#SBATCH -t {0}:00:00\n".format(Options.m_time))
    if Options.m_exclude != 0:
        
        nodes = GetSlurmNodes()
        random.shuffle(nodes)
        nodes = nodes[0:int(opts.m_exclude)]
        
        nodes2exclude = ""
        for n in nodes:
            if n == nodes[-1]: nodes2exclude += n
            else: nodes2exclude += n +","
                
        fo.write("#SBATCH --exclude={0}\n\n\n".format(nodes2exclude))
    
    fo.write(oldrunstr)
    fo.close()
    
    command = "sbatch "+Dirname+"/run.sh"
    return command
    
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
    parser.add_argument("-cpu", default=4000, dest="m_cpu", type=int,
        help="Memory per cpu (Slurm).")
    parser.add_argument("-time", default=20, dest="m_time", type=int,
        help="Maximum time of the job in hours (Slurm).")
    parser.add_argument("-exclude", default=0, dest="m_exclude", type=int,
        help="Number of nodes to exclude (Slurm).")
    parser.add_argument("-in", dest="infiles", default = "", help="Files to copy over")
    parser.add_argument("command", help="Command to launch")
    opts = parser.parse_args()
    

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
   
    ########################################################################################
    ## Make the needed folders and copy the executable and everything else needed in them
    ########################################################################################
    
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
            
    ########################################################################################
    ## Create the run.sh file containing the information about how the executable is run
    ########################################################################################

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

    if opts.local or opts.interactive :     ### Output
        runfile.write( " >& " + dirname + "/out " )
    runfile.close()
    os.system( "chmod 755 " + dirname + "/run.sh" )
    
    ########################################################################################
    ## Run executable in local, interactive or batch mode
    ########################################################################################
    
    if(opts.subdir != "") :
        opts.subdir=(re.sub("^.*/","",opts.subdir)+"_")
    
    if opts.local :                           ## Local
        print("Running local")
        command  = "cd " + dirname
        command += dirname + "/run.sh &"
            
    elif "lxplus" in os.getenv("HOSTNAME") :  ## Batch for lxplus
        if opts.interactive :
            command = LaunchInteractive(dirname)
        else :
            command = PrepareLxplusJob(opts, dirname)
            
    elif IsSlurm():
        command = PrepareSlurmJob(opts, dirname)
     
    else :
        print("Can run in batch mode only on lxplus or on a slurm batch system. Go there or run with '--local'")
     
    ########################################################################################
    ## Execution of the job sending
    ########################################################################################
       
    os.system(command)


