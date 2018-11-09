"""
collect phase2 file for selected HST Cycle 26 programs
Proposal Number start from 15490
end in 15664
"""
import urllib
from os import path

url_template = "http://www.stsci.edu/hst/phase2-public/{0}.apt"
DATA_DIR = '../DATA/'

# n_start = 15480
# n_end = 15490
n_start = 0
n_end = 0


for i in range(n_start, n_end):
    url_i = url_template.format(i)
    saveFN = path.join(DATA_DIR, url_i.split('/')[-1])
    print("Retrieving data from: {0}\n Saving to {1}".format(
        url_i, saveFN))
    try:
        urllib.request.urlretrieve(url_i, saveFN)
    except urllib.error.HTTPError:
        print("Program {0} does not exist".format(i))
