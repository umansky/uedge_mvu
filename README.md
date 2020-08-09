# uedge_mvu
* Set of Python tools for UEDGE by M.Umansky *


##-Check out from github:
git clone https://github.com/umansky/uedge_mvu

##-Install:
Set up uedge_mvu as a package by running the following command inside the directory containing `setup.py`:
pip install --editable . --user

This way, you can do `from uedge_mvu import *` from anywhere, and
python will read the files in e.g. `~/Desktop/uedge_mvu`. Note that
this will break and you will need to reinstall if you change the path
of e.g. `~/Desktop/uedge_mvu`.

Python 3 and linux are recommended to avoid bugs.


Usage example:
>python
import uedge_mvu.utils as mu
import uedge_mvu.plot as mp
mu.paws()
mp.plotmesh()
