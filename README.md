[![DOI](https://zenodo.org/badge/109375742.svg)](https://zenodo.org/badge/latestdoi/109375742)

# SimProd

Mini framework to send LHCb simulation jobs on a batch system (HTCondor, Slurm)!

A LHCb mattermost channel called `SimProd` is available for discussing any issues.

## Installation

To install the module do

```
python setup.py install --user
```

You will be asked to enter some directories where you want to find your simulated samples.

### Dependencies:

* [IPython](https://ipython.org)

* [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html)

* [UltraJSON](https://github.com/esnme/ultrajson) (Optionnal, Recommended)

* [setuptools](https://setuptools.readthedocs.io/en/latest/) (Optionnal, Recommended)

## Usage

To launch the module just type `SimProd`.

<p align="center">
<img width="600" height="200"
src="https://github.com/marinang/SimulationProduction/blob/master/etc/begin_interface.png">
</p>

You need to to know:

* the EvtType of the process you want to generate ([DecFiles webpage](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/))

* Year of data taking to simulate (Run I: 2011, 2012, Run II: 2015, 2016, 2017, 2018)

* Number of events you want to produce.

Description of simulation setups can be found [here](https://github.com/marinang/SimulationProduction/tree/master/simprod/simjob/setup). To start a new simulation job do:

```python
>>> j = SimulationJob(evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)
>>> j.prepare()
>>> j.send()
```

<p align="center">
<img width="750" height="300" src="https://github.com/marinang/SimulationProduction/blob/master/etc/submission.png">
</p>


### Options

Your have other options by default that you can change:

* `j.polarity`: Magnet conditions to simulate [MagUp or MagDown, default: half MagUp, half MagDown].

* `j.neventsjob`: Number of events per jobs [default: 50].

* `j.runnumber`: Run number for simulation in Gauss.

* `j.simcond`: Simulation condition [Sim09b, Sim09c, Sim09e, Sim09g, Sim09h default: Sim09h].

* `j.stripping`: Version of the stripping (default = '').

* `j.turbo`: Run the Turbo step.

* `j.mudst`: Produce a muDST output.

* `j.decfiles`: Version of the DecFiles package (default = v30r46).

* `j.infiles`: External files to provide for generation (for example LHE or HepMC files).

* `j.cpu`: Number of CPU memory (in MB) per simulation job.

* `j.keeplogs`: keeps the log files even if the jobs is marked as completed (default = True).

* `j.keepxmls`: keeps the generator log xml files (default = True).

* `j.redecay`: use redecay at generation (default = False).

* `j.simmodel`: "pythia8" or "BcVegPy" (default = "pythia8").

These argument are also available at instantiation of a SimulationJob but also as property, i.e:

```python
>>> j = SimulationJob(evttype=EVTTYPE, year=YEAR, nevents=NEVENTS, neventsjob=NEVENTSJOB)
```

is equivalent to

```python
>>> j = SimulationJob(evttype=EVTTYPE, year=YEAR, nevents=NEVENTS)
>>> j.neventsjob = NEVENTSJOB
```

you can also modify options for the scheduler you are using through
```
>>> j.deliveryclerk
```

#### HTCondor options

Options for htcondor batch system:

* `j.deliveryclerk.jobflavour`: flavour of a job correspoinding to a maximum runtime (default = "workday").

The available job flavours are as follows:

```
    espresso     = 20 minutes
    microcentury = 1 hour
    longlunch    = 2 hours
    workday      = 8 hours
    tomorrow     = 1 day
    testmatch    = 3 days
    nextweek     = 1 week
```

#### Slurm options

Options for slurm batch system with default values designed for EPFL usage:

* `j.deliveryclerk.time`: Maximum running time per simulation job in hours.

* `j.deliveryclerk.nsimjobs`: Maximum number of simultaneous simulation jobs running.

* `j.deliveryclerk.nsimuserjobs`: Maximum number of simultaneous simulation jobs running for the user.

* `j.deliveryclerk.nuserjobs`: Maximum number of simultaneous jobs running for the user.

* `j.deliveryclerk.npendingjobs`: Maximum number of pending jobs for the user.

* `j.deliveryclerk.nfreenodes`: Number of nodes to be free of user's simulation jobs.

* `j.deliveryclerk.subtime`: Time interval when the jobs are sent (e.g. 16 18 means from 4pm to 6pm).

If using the EPFL cluster, please avoid using these options, a configuration file is read with agreed values for these options.

[PySlurm](https://github.com/PySlurm/pyslurm/wiki/Installing-PySlurm) can be installed for faster monitoring of the jobs.


## Monitoring

Just after the lauching the program type `jobs` and you can see the status of submitted jobs:

<p align="center">
<img width="540" height="500" src="https://github.com/marinang/SimulationProduction/blob/master/etc/monitor.png">
</p>

### Resend failed subjobs

Use the SimulationJob method **send**:
```python
>>> jobs[JOBNUMBER].send()
```
This will send only unsubmitted and failed jobs.

### Kill a subjob

```python
>>> jobs[JOBNUMBER][SUBJOBNUMBER].kill()
```

### Remove jobs from the collection

If you wish to remove a job from the `jobs` container do

```python
>>> jobs[JOBNUMBER].remove()
```
and the simulation job will not be seen anymore when typing `jobs`. Note that if subjobs are still running they will be killed.

If you wish to remove only completed jobs do

```python
>>> for j in jobs.select("completed"):
>>>     j.remove()
```
The log files are also with removed with the job.

## Evttypes

For generation Gauss needs an option file callled EVTTYPE.py which is stored in a folder called **Evttypes**. In you need to modify your option file prior to submission you can type in the `SimProd` prompt

```python
>>> getevttype(EVTTYPE)
```

and all option files related to this EVTTYPE should be downloaded into the **Evttypes** directory.

## Where are the simulated samples stored?
One the jobs are marked as successfully completed you should find the simulated `dst` files in the production directory printed when you start `SimProd`.
You can also retrieve the production directory by typing in the prompt

```python
>>> simoutput
'/eos/lhcb/user/m/mmarinan/SimulationJobs'
```

The `dst` are then stored in `EVTTYPE/YEAR/SIMCOND/POLARITY`, see for instance the following example of the tree of the directories in the production directory:
```markdown
- SimulationJobs
    - EVTTYPE_1
        - 2016
            - Sim09h
                - MagUp
                    - xml
                        - 1234567.xml
                        - ...
                        - 1891234.dst
                    - 50evts_s28r2_1234567.dst
                    - ...
                    - 50evts_s28r2_1891234.dst
                - MagDown
                    - xml
                        - 2345671.xml
                        - ...
                        - 8912342.dst
                    - 50evts_s28r2_2345671.dst
                    - ...
                    - 50evts_s28r2_8912342.dst

    - EVTTYPE_2
        - 2018
            - Sim09g
                - MagUp
                    - xml
                    - 50evts_s34_3456712.dst
                    - ...
                    - 50evts_s34_9123418.dst
                - MagDown
                    - xml
                    - 50evts_s34_5345671.dst
                    - ...
                    - 50evts_s34_6912342.dst
```

The `dst` files are named `NEVENTSJOBevts_STRIPPING_RUNNUMBER.(m)dst`. In the `xml` directory are stored the `RUNNUMBER.xml` files which contain informations of event generation such as the generator level efficiency. The generator level informations of your jobs are stored only if `j.keepxmls == True`.

To analyse your simulated samples you can create ROOT ntuples using the `dst` files. The [LHCb starterkit](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/minimal-dv-job.html) explains how to do a local `DaVinci` job with local `dst` files.


## Contributing

Feel free to contribute by the mean of Pull Requests.
