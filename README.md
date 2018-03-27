# Simulation production

Mini framework to send LHCb simulation jobs on a batch system (LSF or Slurm)!

## Installation

To install the module do

`$ python setup.py install (--user)`.

You will be asked to enter some directories where you want to find your simulated samples.

## Usage

To launch the module just type `$ simprod`.

<p align="center">
<img width="600" height="200" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/begin_interface.png">
</p>

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases/dev/table_evttype.php))	

* Year of data taking to simulate (Run I: 2011, 2012, Run II: 2015, 2016, 2017)

* Number of events you want to produce.

Description of simulation setups can be found [here](https://github.com/marinang/SimulationProduction/tree/master/simjob/setup). To start a new simulation job do:

`$ j = SimulationJob( evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)`

`$ j.prepare()`

`$ j.send()`

<p align="center">
<img width="750" height="300" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/submission.png">
</p>

You can also launch a job by doing:

`$ simprod --evttype EVTTYPE --year YEAR --nevents NEVENTS`

### Options

Your have other options by default that you can change:

* polarity: Magnet conditions to simulate [MagUp or MagDown, default: half MagUp, half MagDown].

* neventsjob: Number of events per jobs [default: 50]. 

* runnumber: Run number for simulation in Gauss.

* simcond: Simulation condition [Sim09b, Sim09c, default: Sim09c].

* stripping: Version of the stripping (default = '').

* turbo: Run the Turbo step (output not test).

* mudst: Produce a muDST output.

* decfiles: Version of the DecFiles package (default = v30r5)

* infiles: External files to provide for generation (for example LHE or HepMC files).

* cpu: Number of CPU memory (in MB) per simulation job.
	
These argument are all available at instantiation of a SimulationJob but also as property, i.e:

`$ j = SimulationJob( evttype=EVTTYPE, year=YEAR, nevents=NEVENTS, neventsjob=NEVENTSJOB)`

is equivalent to

`$ j = SimulationJob( evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)`

### Slurm options

You have additionnal options for slurm batch system with default values designed for EPFL usage.

* time: Maximum running time per simulation job in hours.

* nsimjobs: Maximum number of simultaneous simulation jobs running.
		
* nsimuserjobs: Maximum number of simultaneous simulation jobs running for the user.
												
* nuserjobs: Maximum number of simultaneous jobs running for the user.
												
* npendingjobs: Maximum number of pending jobs for the user.

* nfreenodes: Number of nodes to be free of user's simulation jobs.
		
* subtime: Time interval when the jobs are sent (e.g. 16 18 means from 4pm to 6pm).

## Monitoring

Just after the lauching the program type `jobs` and you can see the status of submitted jobs:

<p align="center">
<img width="540" height="500" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/monitor.png">
</p>
