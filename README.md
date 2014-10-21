## Quick cleaner ##

I have a directory containing many c# solutions/projects.
This cleaner deletes all bin/obj files (and some other ones).

All my projects are stored in git repositories, and so
I just make use of ``git clean -xfd``.

This program will run through all directories in my root directory searching for the .git folder then run the above command.


### Dependencies ###
- Python 2.7

- [GitPython](https://pythonhosted.org/GitPython/0.3.1/intro.html#installing-gitpython)
 