import os


class RootError(Exception):
    def __init__(self, value):
        self.value = value

# variables
pipeline_root = ''
# get pipeline_root from config.txt, line 1

with open('config.txt', 'w') as f:
    pipeline_root = f.readline().split('#')[0]
    pipeline_root.strip()

if os.path.isdir(pipeline_root) == False
    raise RootError('pipeline_root not a valid directory.')

#directories used in pipeline
scampdir = pipeline_root + 'scampdir'
swarpdir = pipeline_root + 'swarpdir'
sexdir = pipeline_root + 'sexdir'
fitsdir = pipeline_root + 'fitsdir'
finished_catalogs = pipeline_root + 'finished_catalogs'
finished_stacked = pipeline_root + 'finished_stacked'
finished_fits = pipeline_root + 'finished_fits'
target_data = pipeline_root + 'target_data'
dirlists = [astrometry, stacking, sex, finished_catalogs, finished_stacked, target_data]

if __name__ == '__main__':
    # if config.py is ran as main script, then makedirs() is executed
    for i in dirlists:
        try:
            os.mkdir(i)
        except FileExistsError:
            print(i, 'already exists.')
        except:
            raise
