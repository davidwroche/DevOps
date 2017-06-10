#!/usr/bin/python3

#@author: David-Roche
#@date: 27/10/2016

# Script to check if NGINX is running or not.

# We will scp it upto the the instance and get back a value from
# which we can determine if it is running or not.

# If not we start it

import sys
import subprocess
import time


def checknginx():
    cmd = 'ps -A | grep nginx'
    (status,output) = subprocess.getstatusoutput(cmd)

    if status > 0:
        print('Nginx server is not running')
        time.sleep(2)
        print('We will start it now!')
        check = 'sudo service nginx start'
        (status,output) = subprocess.getstatusoutput(check)
    else:
        print('Nginx server is running')

checknginx()