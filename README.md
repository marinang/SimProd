# SimulationProduction

Mini framework to send simulation jobs into a slurm batch system!

You need to to know:

	- the EvtType of the process you want to generate
	( http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/releases/dev/table_evttype.php )
	- Year of data taking to simulate (Run I: 2012, Run II: 2015, 2016)

	- Number of events you want to produce
	
Before launching make sure that you set the environnemnt variable "SIMOUTPUT" to the path of where you want to save the outputs of the jobs. This can be done using the setup script by doing "source steup.sh".

The script to launch jobs is "LaunchProduction.py", usage:

	LaunchProduction.py [-h][--polarity <polarity>]
							[--neventsjobs <neventsjobs>]
							[--runnumber <runnumber>] [--nsimjobs <nsimjobs>]
							[--nsimuserjobs <nsimjobs>]
							[--nuserjobs <nuserjobs>]
							[--npendingjobs <npendingjobs>]
							[--subtime <subtime> [<subtime> ...]]
							<evttype> <nevents> <year>

positional arguments:

	<evttype>            EvtType of the processus to generate
	<nevents>            Number of events to produce
	<year>               Year to simulate

optional arguments:

	-h, --help            show this help message and exit
	
	--polarity <polarity>	     Magnet conditions to simulate.
	
	--neventsjobs <neventsjobs>	 Number of events per jobs.
	
	--runnumber <runnumber>		 Run number for Gauss.
	
	--nsimjobs <nsimjobs>		 Maximum number of simultaneous simulation jobs running.
	
	--nsimuserjobs <nsimjobs>	 Maximum number of simultaneous simulation jobs running for the user.
												
	--nuserjobs <nuserjobs>		 Maximum number of simultaneous jobs running for the user.
												
	--npendingjobs <npendingjobs>   Maximum number of pending jobs for the user.
	
	--subtime <subtime> [<subtime> ...]	 Time interval when the jobs are sent.
