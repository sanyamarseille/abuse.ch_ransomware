#!/usr/bin/env python
#coding:UTF-8

##### NOTE ######
# Ransumeware URL list
#################

## set constant
# Database Server URL
URL = 'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt'

## download file path and filename
download_path = './'
download_filename = 'ransomeware_malicious_list.txt'

## import module
import urllib2

## main code
response = urllib2.urlopen(URL)

file = open(download_path + download_filename,'w')

for line in response:
    if line.find('#') == 0:
        continue
    #file.write(line)
    file.write(line.strip('http://'))

file.close()