#!/usr/bin/python3

#@author: David-Roche
#@date: 27/10/2016

# This script is used to launch a new AWS instance. It takes in the users Key & path to their key.
# It asks the user to create a Security group name. If the user leaves it blank the script sets the 
# default security group name. It creates the instance and lets the user update this, install python35,
# install Nginx and then upload their check_webserver script to instance and check if Nginx is running.

# As additional functionality we have created a class called printclass which handles all the print statments 
# in the the script. I have also implmented a Logger function which logs invalids options, errors and 
# output from commands to the monitor.txt file.

# I have enabled a user to terminate an instance once they have created it. A user can install a mysql server,
# set root password and create a database. A user can also install sys stat on the instance and run a command
# which will give cpu usage back to the command line. For each of these commands you will be able to see the
# output in the monitor.txt file. 

import sys
import time
import boto
import boto.ec2
import os.path
import os
import subprocess
import Logger
from printclass import printStatements

# Global Variables which will be resused throughout the script
namekey = ''
ip = ''
path = ''
groupname = ''
point = ''
instance = ''

#We create a new instance of the class and call it printThis
printThis = printStatements()


# We want to check whether our script to check the webserver exists or not
def check_file_exists():

    # We call the print statements from the class
    printThis.get_1()
    printThis.get_2()
    # The filename which should be found in our current directory
    filename = './'+'check_webserver.py'

    # We check whether this file is within the directory
    if not os.path.isfile(filename):
        Logger.logger.info('check_webserver.py file does not exists within this directory')
        printThis.get_3()
        printThis.get_4()
    else:
        printThis.get_5()
        printThis.newline()
        checkKeyPath()
        return True


# Update the system clock and calls the next script
def clockupdate():
    printThis.get_6()
    os.system('sudo ntpdate ntp.ubuntu.com')
    printThis.newline()
    check_file_exists()

# Check key & path are correct
def checkKeyPath():
    global path
    global namekey

    # Inputs which take in user values
    key = input('Please input the name of your key : ')
    time.sleep(2)
    path = input('Please input the path to your key : ')

    # Concat the path provided with the keyname
    checkkey = str(path) + str(key)+'.pem'
    

    # Checks the path for the key for a match
    if not os.path.isfile(checkkey):
        Logger.logger.info(str(key)+'.pem' +' file does not exists within this directory')
        printThis.get_7()
        printThis.get_8()
        printThis.get_9()
        printThis.newline()
    else:
        printThis.get_10()
        printThis.newline()
        namekey = str(key)
        create()
        return True

# Function to create an aws instance and store data in global variables for reuse.
def create():
    global ip
    global groupname
    global instance

    # We will try create a new security group with the name entered from the user otherwise we use a default groupname
    try:
        secgroupname = input('\033[1;33m What would you like to call your security group? : \033[1;m')
        if len(str(secgroupname)) > 0:
            print('Setting your security group name to ' + str(secgroupname))
            printThis.newline()
            global groupname
            groupname = str(secgroupname)
        else:
            groupname = 'sshhttpmysql'
        conn = boto.ec2.connect_to_region('us-west-2')
        secgroup = conn.create_security_group(str(groupname), 'HTTP, MYSQL & SSH')
        secgroup.authorize('tcp', 80, 80, '0.0.0.0/0') #HTTP
        secgroup.authorize('tcp', 22, 22, '0.0.0.0/0') #SSH
        secgroup.authorize('tcp', 3306, 3306, '0.0.0.0/0') #MYSQL
        print('Added Security Group : ' + str(groupname))
    except:
        print('Security group ' + str(groupname) + ' already exists!!')
        Logger.logger.info('Security group' + str(groupname) + 'already exists!!')
        printThis.get_11()

    reservation = conn.run_instances('ami-7172b611', key_name = str(namekey), instance_type = 't2.micro', security_groups = [str(groupname)])

    instance = reservation.instances[0]
    printThis.get_12()

    # We wait for the instance to run
    while instance.state != 'running':
        time.sleep(3)
        instance.update()
        printThis.get_13()
    else:
    # When it does run we get the ip from it
        printThis.newline()
        print('Your instance is ' + instance.state)
        time.sleep(5)
        ip = instance.ip_address
        print('Your ip address is ' + ip)
        time.sleep(5)
        main()


# We call this once the instance has been created to update the instance, install python on it and install nginx
def instanceip():
    # We first check if an instance has been created by checking the global variable ip
    if len(ip) < 1:
        printThis.get_15()
        printThis.get_16()
        main()
    else:
        global point
        point = 'reached'
        printThis.get_17()
        printThis.get_18()
   
    # We run these commands and wait for them to complete
    update = ' sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo yum -y update' "
    time.sleep(1)
    py = ' sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo yum -y install python35' "
    time.sleep(2)
    ngin = ' sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo yum -y install nginx' "
    time.sleep(2)

    # We log the output of each command out to the logger file
    (status, output) = subprocess.getstatusoutput(update)
    Logger.logger.info('Turned on mysql-server' + str(output))
    printThis.get_19()
    (status, output) = subprocess.getstatusoutput(py)
    Logger.logger.info('Turned on mysql-server' + str(output))
    printThis.get_20()
    (status, output) = subprocess.getstatusoutput(ngin)
    Logger.logger.info('Turned on mysql-server' + str(output))
    printThis.get_21()
    push_nginx()

# Terminate the instance and reset the global ip to an empty string
def terminate():
    if len(ip) < 1:
        print('\033[1;41m You need to create an instance first \033[1;m')
        time.sleep(2)
        print('Returning to menu')
        time.sleep(1)
        main()
    else:
        print('Terminating your instance!')
        instance.terminate()
        global ip
        ip = ''
        main()

# We push the local file we checked for at the start of our script to the server and make it executable
def push_nginx():
    printThis.get_22()

    filename = 'check_webserver.py'

    cmd = "scp -i " + path + namekey + ".pem" + " " + filename + " " + 'ec2-user@' + ip + ':/home/ec2-user'
    (status, output) = subprocess.getstatusoutput(cmd)

    change = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " ' chmod 700 check_webserver.py ' "
    (status, output) = subprocess.getstatusoutput(change)

    execute = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " ' ./check_webserver.py ' "
    (status, output) = subprocess.getstatusoutput(execute)

    printThis.get_23()
    # We check the status we get back from the script run on the server
    if status == 0:
        printThis.get_24()
        main()
    else:
        printThis.get_25()
        main()

# Install mysql server, set root password and create a database
def mysql():
    # We check the length of the ip, if its greater than 1 in length we know an ip has been set and an instance has been created
    if len(ip) < 1:
        printThis.get_26()
        main()

    if point != 'reached':
        printThis.get_27()

    # We install the mysql server
    install = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo yum -y install mysql-server' "
    (status, output) = subprocess.getstatusoutput(install)
    printThis.get_28()
    Logger.logger.info('Instaled mysql-server' + str(output))

    # We check the configuration of the server and turn it on
    on = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo chkconfig mysqld on' "
    (status, output) = subprocess.getstatusoutput(on)
    printThis.get_29()
    Logger.logger.info('Turned on mysql-server' + str(output))

    # We start the mysql server
    start = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo service mysqld start' "
    (status, output) = subprocess.getstatusoutput(start)
    printThis.get_30()
    Logger.logger.info('Starting mysql-server ' + str(output))

    # We ask the user what password they would to set for the root user
    printThis.get_31()
    password = input('Input the password you would like :')

    # We then set the root password
    root = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'mysqladmin -u root password '"+ str(password) 
    (status, output) = subprocess.getstatusoutput(root)
    Logger.logger.info('Setting root password to ' + str(password))
    printThis.get_32()
    
    # We ask the user what they would like to call the database
    dbname = input('Input the name for the new database :')

    db = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'mysqladmin -u root -p create '"+ str(dbname) 
    (status, output) = subprocess.getstatusoutput(db)
    printThis.get_33()
    Logger.logger.info('Creating a database with the name ' + str(dbname))
    main()

#Install sysstat to get more information about the cpu usage on the instance
def cpu():
    # We check the length of the ip, if its greater than 1 in length we know an ip has been set and an instance has been created
    if len(ip) < 1:
        printThis.get_26()
        main()

    if point != 'reached':
        printThis.get_40()

    # We install htop on the instance to monitor system usage
    stat = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'sudo yum -y install sysstat' "
    (status, output) = subprocess.getstatusoutput(stat)
    Logger.logger.info('Installing sysstat ' + str(output))

    # We execute the htop command to display the utilization of each cpu
    mp = 'sudo ssh -t -o StrictHostKeyChecking=no -i ' + path + namekey + ".pem" + " " + 'ec2-user@' + ip + " 'mpstat' "
    (status, output) = subprocess.getstatusoutput(mp)
    printThis.get_36()
    Logger.logger.info('Running htop ' + str(output))
    print(output)

    main()


# Our Main menu through which various portions of the script are called
def main():
    printThis.get_37()
    question = input(' \033[5;41;32m Input:>> \033[0m ')
    while question != "exit":
        if question == '1':
            clockupdate()
        elif question == '2':
             instanceip()
        elif question == '3':
             mysql() 
        elif question == '4':
             cpu()
        elif question == '5':
             terminate()
        else:
            Logger.logger.info('You have selected an invalid menu option')
            printThis.get_38()
            main ()
    else:
        printThis.get_39()


if __name__ == '__main__':
        main()


