# Simulation production

Mini framework to send simulation jobs into lxplus or a slurm batch system!

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases/dev/table_evttype.php))	

* Year of data taking to simulate (Run I: 2012, Run II: 2015, 2016)

* Number of events you want to produce.
	
Before launching make sure that you set the environnement variable _$SIMOUTPUT_ to the path of where you want to save the outputs of the jobs. This can be done using the setup script by doing "source setup.sh" or adding this variable to your _.bashrc_.

The script to launch jobs is **LaunchProduction.py**, usage: LaunchProduction.py EvtType Year #Events

optional arguments:

* --polarity: Magnet conditions to simulate.

* --neventsjobs: Number of events per jobs.

* --runnumber: Run number for Gauss.
	
If you wish to modify any option related to an EvtType prior to launch submission, the **GetEvtType.py** script will copy every option file that are in _EvtType.py_ to a directory called _EvtTypes_. It takes the EvtType as argument.

If you wish to send jobs on a **Slurm** batch system you can add the following options for **LaunchProduction.py**

* --nsimjobs: Maximum number of simultaneous simulation jobs running.
		
* --nsimuserjobs: Maximum number of simultaneous simulation jobs running for the user.
												
* --nuserjobs: Maximum number of simultaneous jobs running for the user.
												
* --npendingjobs: Maximum number of pending jobs for the user.
		
* --subtime: Time interval when the jobs are sent (e.g. 16 18 means from 4pm to 8pm).