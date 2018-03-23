# Simulation production

Mini framework to send LHCb simulation jobs on a batch system (LSF or Slurm)!

## Installation

To install the module do

`$ python setup.py install`.

You will be asked to enter some directories where you want to find your simulated samples.

## Usage

To launch the module just type `$ simprod`.

->![start](/etc/begin_interface.jpeg?raw=true =600x200)<-

[//]: # ->![alt text](https://github.com/marinang/SimulationProduction/blob/userinterface/etc/begin_interface.png?raw=true =600x200)<-

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases/dev/table_evttype.php))	

* Year of data taking to simulate (Run I: 2011, 2012, Run II: 2015, 2016, 2017)

* Number of events you want to produce.

Description of simulation setups can be found [here](https://github.com/marinang/SimulationProduction/tree/master/simjob/setup). To start a new simulation job do:

`$ j = SimulationJob(evttype = EVTTYPE, year = YEAR, nevents = NEVENTS)`
`$ j.prepare()`
`$ j.send()`

->![submission](/etc/submission.jpeg?raw=true =600x200)<-

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
