#!/bin/bash

mkdir -p formatted-data
find raw-data/* | xargs -I {} python formatter.py --outdir=formatted-data --filename={}