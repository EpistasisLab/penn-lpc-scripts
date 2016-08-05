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

# Counts your jobs: running, pending, and total

proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
out = out.decode('utf-8') 

job_count = 0
running_count = 0
pending_count = 0

for line in out.split('\n'):
    # Change 'moore_' to the name of your lab's queue
    if 'moore_' in line:
        job_count += 1
    if 'RUN' in line:
        running_count += 1
    if 'PEND' in line or 'SSUSP' in line:
        pending_count += 1

print('\n{} jobs running\n{} jobs queued\n{} jobs total\n'.format(running_count, pending_count, job_count))
