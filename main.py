import os
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

os.system('clear')

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = indeed_jobs + so_jobs

print(jobs)