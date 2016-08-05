# Example scripts for the Penn LPC

This repository contains several scripts and settings that I have developed for use on the Penn LPC.

Feel free to rework and reuse these scripts as you like. If you have a useful addition, please [file an issue](https://github.com/rhiever/penn-lpc-scripts/issues/new) with your suggested change so we can discuss it.

## Files included

* [.bash_profile](.bash_profile): Contains some basic settings and aliases that I found useful on the LPC.

* [bcount.py](bcount.py): Counts your jobs: running, pending, and total

* [bnames.py](bnames.py): Lists counts of all of your job by name

* [example-batch-submission.bsub](example-batch-submission.bsub): Example batch submission script. Use this script if you're submitting several jobs that execute the same commands but need a different random number generator seed.

* [example_job_submitter.py](example_job_submitter.py): Example job submission script. Use this script if you're submitting several jobs that execute similar commands but with varying inputs or parameters. This job submission method has more flexibility than the batch submission method.
