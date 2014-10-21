__author__ = 'yogiv'

import os
from git import *

rootdir = 'C:/Projects7'

for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        if dir == '.git':
            print os.path.join(subdir, dir)
            repo = Repo(subdir)
            repo.git.clean('-xdf')