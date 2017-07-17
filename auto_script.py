import subprocess as sp
import os
import setup.py

def scamp_auto(files, param=False):
    """
    Run scamp on list 'files'
    """
    os.chdir(setup.pipeline_root)
    catalogs = files.
    scamp_arg = 'scamp @catalogs'
    sp.call()
