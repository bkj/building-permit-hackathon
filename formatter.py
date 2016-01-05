import os
import argparse
import json

# --
# CLI

parser = argparse.ArgumentParser()
parser.add_argument('--filename', action='store', dest='filename')
parser.add_argument('--outdir', action='store', dest='outdir')
args   = parser.parse_args()

# --
# IO

filename = args.filename
outdir   = args.outdir
key      = filename.split('/')[-1].split('.')[0]
outpath  = os.path.join(outdir, key + '.json')
print key

# --
# Function for parsing

def czip(fieldnames, data):
    fn     = [f[0] for f in fieldnames]
    data   = [dict(zip(fn, d)) for d in data]
    nested = filter(lambda x: x[1] != None, fieldnames)
    for n in nested:
        for d in data:
            d[n[0]] = dict(zip(n[1], d[n[0]]))
    
    return data

# --
# Load

x    = json.load(open(filename))
meta = x['meta']['view']['columns']
data = x['data']

# -- 
# Format

fieldnames = [(m['fieldName'], m.get('subColumnTypes', None)) for m in meta]
formatted  = czip(fieldnames, data)

# --
# Write to file

json.dump(dict([(key, formatted)]), open(outpath, 'wb'), indent = 4)