# Simulation production

Mini framework to send LHCb simulation jobs on a batch system (HTCondor, LSF or Slurm)!

## Installation

To install the module do

```
python setup.py install --user
```

You will be asked to enter some directories where you want to find your simulated samples.

### Dependencies:

* [IPython](https://ipython.org)

* [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html)

* [PySlurm](https://github.com/PySlurm/pyslurm/wiki/Installing-PySlurm)  (Optionnal, only if in a Slurm batch system).

* [UltraJSON](https://github.com/esnme/ultrajson)  (Optionnal, Recommended).

## Usage

To launch the module just type `simprod`.

<p align="center">
<img width="600" height="200" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/begin_interface.png">
</p>

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/))	

* Year of data taking to simulate (Run I: 2011, 2012, Run II: 2015, 2016, 2017)

* Number of events you want to produce.

Description of simulation setups can be found [here](https://github.com/marinang/SimulationProduction/tree/master/simprod/simjob/setup). To start a new simulation job do:

```python 
j = SimulationJob( evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)
j.prepare()
j.send()
```

<p align="center">
<img width="750" height="300" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/submission.png">
</p>

You can also launch a job by doing:

```
simprod --evttype EVTTYPE --year YEAR --nevents NEVENTS
```

### Options

Your have other options by default that you can change:

* polarity: Magnet conditions to simulate [MagUp or MagDown, default: half MagUp, half MagDown].

* neventsjob: Number of events per jobs [default: 50]. 

* runnumber: Run number for simulation in Gauss.

* simcond: Simulation condition [Sim09b, Sim09c, Sim09e, default: Sim09e].

* stripping: Version of the stripping (default = '').

* turbo: Run the Turbo step (output not tested).

* mudst: Produce a muDST output.

* decfiles: Version of the DecFiles package (default = v30r25).

* infiles: External files to provide for generation (for example LHE or HepMC files).

* cpu: Number of CPU memory (in MB) per simulation job.

* keeplogs: keeps the log files even if the jobs is marked as completed (default = True).

* keepxmls: keeps the generator log xml files (default = True).

* redecay: use redecay at generation (default = False).
	
These argument are all available at instantiation of a SimulationJob but also as property, i.e:

```python 
j = SimulationJob(evttype=EVTTYPE, year=YEAR, nevents=NEVENTS, neventsjob=NEVENTSJOB)
```

is equivalent to

```python 
j = SimulationJob(evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)
j.neventsjob = NEVENTSJOB
```

### Slurm options

You have additionnal options for slurm batch system with default values designed for EPFL usage.

* time: Maximum running time per simulation job in hours.

* nsimjobs: Maximum number of simultaneous simulation jobs running.
		
* nsimuserjobs: Maximum number of simultaneous simulation jobs running for the user.
												
* nuserjobs: Maximum number of simultaneous jobs running for the user.
												
* npendingjobs: Maximum number of pending jobs for the user.

* nfreenodes: Number of nodes to be free of user's simulation jobs.
		
* subtime: Time interval when the jobs are sent (e.g. 16 18 means from 4pm to 6pm).

If using the EPFL cluster, please avoid using these options, a configuration file is read with agreed values for these options.

## Monitoring

Just after the lauching the program type `jobs` and you can see the status of submitted jobs:

<p align="center">
<img width="540" height="500" src="https://github.com/marinang/SimulationProduction/blob/userinterface/etc/monitor.png">
</p>

### Resend failed subjobs

Use the SimulationJob method **send**:
```python 
jobs[JOBNUMBER].resend()
```
This will send only unsubmitted and failed jobs.

### Kill a subjob

```python 
jobs[JOBNUMBER][SUBJOBNUMBER].kill()
```

### Remove jobs from the collection

If you wish to remove a job from the `jobs` container do

```python 
jobs[JOBNUMBER].remove()
```
and the simulation job will not be seen anymore when typing `jobs`. Note that if subjobs are still running they will be killed.

If you wish to remove only completed jobs do

```python 
for j in jobs.select("completed"):
    j.remove()
```
The log files are also with removed with the job.

## Evttypes

For generation Gauss needs an option file callled EVTTYPE.py which is stored in a folder called **Evttypes**. In you need to modify your option file prior to submission you can type in the simprod prompt 

```python
getevttype(EVTTYPE)
```

and all option files related to this EVTTYPE should be downloaded into the **Evttypes** directory.

## Contributing

Feel free to contribute by the mean of Pull Requests.
