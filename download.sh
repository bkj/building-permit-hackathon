#!/bin/bash

mkdir -p raw-data
awk -F "/" '{OFS="|"; system("wget --no-check-certificate -O raw-data/" $6 ".json " $0)}' paths.txt
