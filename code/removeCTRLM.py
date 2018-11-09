import tempfile
from os import path
import os
import glob


def removeCTRLM(filename):

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as fh:
        for line in open(filename):
            line = line.rstrip()
            fh.write(line + '\n')
        os.rename(filename, filename + '.bak')
        os.rename(fh.name, filename)


if __name__ == '__main__':
    fns = glob.glob('../DATA/*.apt')
    for fn in fns:
        removeCTRLM(fn)
