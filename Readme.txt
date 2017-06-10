#!/usr/bin/python3

#@author: David-Roche
#@date: 27/10/2016

# The run_newwebserver.py script is used to launch a new AWS instance. It takes in the users Key & path to their key.
# It asks the user to create a Security group name. If the user leaves it blank the script sets the 
# default security group name. It creates the instance and lets the user update this, install python35,
# install Nginx and then upload their check_webserver script to instance and check if Nginx is running.

# As additional functionality we have created a class called printclass.py which handles all the print statments 
# in the the script. I have also implmented a Logger.py script which logs invalids options, errors and 
# output from commands to the monitor.txt file.

# I have enabled a user to terminate an instance once they have created it. A user can install a mysql server,
# set root password and create a database. A user can also install sys stat on the instance and run a command
# which will give cpu usage back to the command line. For each of these commands you will be able to see the
# output in the monitor.txt file. 

# I have incorporated a menu system which guides the user through the set up. The menu checks for invalid entries
# and will let the user know if they try and skip any steps.


