# -*- coding: utf-8 -*-                                                                                                           

"""                                                                                                                               
Copyright (c) 2016 Randal S. Olson                                                                                                
                                                                                                                                  
Permission is hereby granted, free of charge, to any person obtaining a copy of this software                                     
and associated documentation files (the "Software"), to deal in the Software without restriction,                                 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,                             
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,                             
subject to the following conditions:                                                                                              
                                                                                                                                  
The above copyright notice and this permission notice shall be included in all copies or substantial                              
portions of the Software.                                                                                                         
                                                                                                                                  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT                             
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.                               
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,                           
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE                               
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                                                            
"""

from __future__ import print_function
import os
from glob import glob
import random
import sys

"""
This script generates bsub calls to submit jobs to the LPC one job at a time. Thus, this script
is useful for when you're submitting many jobs that have varying parameters, such as different
data sets or parameter settings.
"""

for dataset in glob('my_data/*.csv'):
    job_num = random.randint(1, sys.maxsize)
    dataset_name = dataset.split('/')[-1].split('.')[0]
    print(dataset_name)

    for job_seed in range(1, 11):
        out_file = 'example-job-{DATASET}-{JOB_NUM}[{JOB_SEED}].out'.format(DATASET=dataset_name,
                                                                            JOB_NUM=job_num,
                                                                            JOB_SEED=job_seed)
        error_file = 'example-job-{DATASET}-{JOB_NUM}[{JOB_SEED}].err'.format(DATASET=dataset_name,
                                                                              JOB_NUM=job_num,
                                                                              JOB_SEED=job_seed)
        job_name = 'example-job-{DATASET}-{JOB_NUM}[{JOB_SEED}]'.format(DATASET=dataset_name,
                                                                        JOB_NUM=job_num,
                                                                        JOB_SEED=job_seed)

        # Make sure to place the commands in quotes and separate the commands with semicolons
        bjob_line = ('bsub -o {OUT_FILE} -e {ERROR_FILE} -J {JOB_NAME} '
                     '"echo "{JOB_SEED}"; cat {DATASET}"'.format(OUT_FILE=out_file,
                                                             ERROR_FILE=error_file,
                                                             JOB_NAME=job_name,
                                                             DATASET=dataset,
                                                             JOB_SEED=str(job_seed).zfill(2)))
        #print(bjob_line)
        os.system(bjob_line)
