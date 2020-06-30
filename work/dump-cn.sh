#!/bin/bash

for ip in $(cat $1); do echo "Scanning $ip..."; cn=$(timeout 2 python3 dumpCN.py "$ip"); echo "{\"ip\":\"$ip\", \"cn\":\"$cn\"}" | jq | tee -a results.txt; done
