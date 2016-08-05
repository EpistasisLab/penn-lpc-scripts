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
import subprocess
from collections import defaultdict

# Lists counts of all of your job by name

proc = subprocess.Popen(['bhist -rl'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
out = out.decode('utf-8') 

job_counts = defaultdict(int)

for line in out.split('\n'):
    if 'Job Name' in line:
        job_name = line.split('<')[2]
        job_name = job_name.split('>')[0].split('[')[0]
        job_counts[job_name] += 1

print('jobs running:')
for job_name in sorted(job_counts):
    print('\t{}{}'.format((job_name + ('.' * 500))[:60], job_counts[job_name]))
