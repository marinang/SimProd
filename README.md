# Simulation production

Mini framework to send simulation jobs into lxplus or a slurm batch system (with access to cvmfs)!

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases/dev/table_evttype.php))	

* Year of data taking to simulate (Run I: 2011, 2012, Run II: 2015, 2016, 2017)

* Number of events you want to produce.

Description of simulation setups can be found [here](https://github.com/marinang/SimulationProduction/tree/master/setup).
	
Before launching make sure to set the environnement variable _$SIMOUTPUT_ to the path of where you want to save the outputs of the jobs. This can be done using the _setup.sh_ script or adding this variable to your _.bashrc_.

The script to launch jobs is **LaunchProduction.py**, usage: python LaunchProduction.py EvtType Year #Events

optional arguments:

* --polarity: Magnet conditions to simulate [MagUp or MagDown, default: half MagUp, half MagDown].

* --neventsjob: Number of events per jobs [default: 50]. 

* --runnumber: Run number for Gauss.

* --simcond: Simulation condition [Sim09b, Sim09c (Preliminary), default: Sim09b].

* --stripping: Version of the stripping (default = '').

* --turbo: Run the Turbo step (output has never been tested).

* --mudst: Produce a muDST output.

* --decfiles: Version of the DecFiles package (default = v30r5)

* --infiles: External files to provide for generation (for example LHE or HepMC files).
	
If you wish to modify any option related to an EvtType prior to launch submission, the **GetEvtType.py** script will copy every option file that are in _EvtType.py_ to a directory called _EvtTypes_. It takes the EvtType as argument.

If you wish to send jobs on a **Slurm** batch system you can add the following options for **LaunchProduction.py**.

* --cpu: Number of CPUs per simulation job.

* --time: Maximum running time per simulation job in hours.

* --nsimjobs: Maximum number of simultaneous simulation jobs running.
		
* --nsimuserjobs: Maximum number of simultaneous simulation jobs running for the user.
												
* --nuserjobs: Maximum number of simultaneous jobs running for the user.
												
* --npendingjobs: Maximum number of pending jobs for the user.

* --nfreenodes: Number of nodes to be free of user's simulation jobs.
		
* --subtime: Time interval when the jobs are sent (e.g. 16 18 means from 4pm to 6pm).

Note you would use these options in a **screen** session, usage: screen python LaunchProduction.py ....
