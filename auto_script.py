import subprocess as sp
import os
import shutil
import glob
import setup.py


class StepNumbError(Exception):
    def __init__(self, value):
        self.value = value


def scamp_auto(files):
    """
    Run Scamp on list 'files'  'files' is a Python list consisting of .fits file names to be sextracted.
    """
    for f in files:
        shutil.move(setup.fitsdir + '/' + f, setup.scampdir + '/' + f)
    os.chdir(setup.scampdir)
    catalogs = open('catalogs.txt', 'w')
    for i in files:
        catalogs.write(i + '\n')
    catalogs.close()
    scamp_arg = 'scamp @catalogs.txt -c configs/coa.scamp'
    try:
        sp.run(scamp_arg, shell=True)
    except:
        raise


def sex_auto(step=1):
    """
    Run SExtractor.  'step' is an integer specifying the step in the pipeline in which sex_auto is being called.  'step=1' is sextracting
    before running scamp, while 'step=2' is assumed to mean sextracting is being done on fits files stacked using Swarp.
    """
    if step==1:
        os.chdir(setup.fitsdir)
    elif step==2:
        os.chdir(setup.swarpdir)
    else:
        raise StepNumbError('Invalid step integer provided.  Must be 1 or 2.')
    for f in glob.glob('*.fit*'):
        shutil.move(os.getcwd + f, setup.sexdir + '/' + f)
    sex_arg = 'sex % -c configs/cao.sex'
    for f in glob.glob('*fit'):
        try:
            sp.run(sex_arg.format(f), shell=True)
        except:
            print(f)
            raise
    
