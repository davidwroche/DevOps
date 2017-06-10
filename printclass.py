#!/usr/bin/python3

#@author: David-Roche
#@date: 27/10/2016

# Class which manages all the print statements or the run_webserver script
# The class has multiple functions which when called returns the specific portion of text 
# that should be printed at that point.

import time
import sys
import os


#A class used to store print statements and functionality attached to each one
class printStatements:
	def __init__(self):
		self.x = ('')
	

	def get_1(self):
		print('\033[1;33m Please make sure the check_webserver file is available in your directory \033[1;m')
		time.sleep(1)

	def get_2(self):
		print('We will now check for this file')
		time.sleep(1)
		 
	def get_3(self):
		print('\033[1;41m file does not exist in this directory \033[1;m')
		 
	def get_4(self):
		print('PLease add this file to your directory and restart the process')
		sys.exit(2)

	def get_5(self):
		print('Your check_webserver script exists')
		
	def get_6(self):
		print('\033[1;33m Going to update your clock to begin with \033[1;m')
		time.sleep(1)

	def get_7(self):
		print('\033[1;41m Your key does not exist in this directory \033[1;m')
		time.sleep(1)

	def get_8(self):
		print('Please make sure you use the correct key')
		time.sleep(1)

	def get_9(self):
		print('Exiting the script')
		sys.exit(2)

	def get_10(self):
		print('\033[1;35m Your key exists in this directory \033[1;m')

	def get_11(self):
		print('Now were going to try create an Instance')
		time.sleep(1)

	def get_12(self):
		print('Please wait while we launch your instance')


	def get_13(self):
		print('Your instance isn\'t running yet' )
		time.sleep(1)


	def get_15(self):
		print('\033[1;41m You need to create an instance first \033[1;m')
		time.sleep(2)

	def get_16(self):
		print('Returning to menu')
		time.sleep(1)


	def get_17(self):
		print('\033[1;33m Going to Update your instance \033[1;m')

	def get_18(self):
		time.sleep(5)
		print('.')
		print('Just waiting for ssh port to open')
		time.sleep(5)
		print('..')
		time.sleep(5)
		print('...')
		time.sleep(5)
		print('....')

	def get_19(self):
		print('Updated Instance')

	def get_20(self):
		print('Installed python35')

	def get_21(self):
		print('Installed Nginx')

	def get_22(self):
		print('Going to push a file to the server and then make it executable')

	def get_23(self):
		print('Check webserver script')

	def get_24(self):
		print('webserver is running')

	def get_25(self):
		print('webserver is not running')

	def get_26(self):
		print('\033[1;41m You need to create an instance first \033[1;m')
		time.sleep(2)
		print('Returning to menu')
		time.sleep(1)


	def get_27(self):
		print('We will now install a mysql server on your instance')
		time.sleep(1)
		time.sleep(5)
		print('.')
		print('Just waiting for ssh port to open')
		time.sleep(5)
		print('..')
		time.sleep(5)
		print('...')
		time.sleep(5)
		print('....')

	def get_28(self):
		print('Installing mysql-server')

	def get_29(self):
		print('Turning the server on')

	def get_30(self):
   		print('Starting the mysql-server')

	def get_31(self):
   		print('Configuring newly installed mysql-server')
   		time.sleep(1)
   		print('Update the password of the root user ')


	def get_32(self):
		print('Setting root password ')
		time.sleep(1)
		print('Create a database')

	def get_33(self):
		print('Creating a database')

	def get_34(self):
		print('We will now install htop on the instance and try gather information on cpu usage')
		time.sleep(1)
		time.sleep(5)
		print('.')
		print('Just waiting for ssh port to open')
		time.sleep(5)
		print('..')
		time.sleep(5)
		print('...')
		time.sleep(5)
		print('....')

	def get_35(self):
		print('Installing htop')

	def get_36(self):
		print('Running htop')

	def get_37(self):
		os.system('clear')
		print ('\033[1;31m Welcome to the Main Menu: \033[1;m' +'\033[1;32m Enter exit to quit  \033[1;m')
		time.sleep(1)
		print ('\033[1;32m Enter 1 \033[1;m' + '\033[1;31m if you would like to create an instance \033[1;m')
		time.sleep(1)
		print ('\033[1;32m Enter 2 \033[1;m' +  '\033[1;31m if you would like to update this instance, push your script to the server \033[1;m')
		time.sleep(1)
		print ('\033[1;32m Enter 3 \033[1;m' +  '\033[1;31m if you would like to install mysql \033[1;m')
		time.sleep(1)
		print ('\033[1;32m Enter 4 \033[1;m' +  '\033[1;31m if you would like to check your instance cpu utilization \033[1;m')
		time.sleep(1)
		print ('\033[1;32m Enter 5 \033[1;m' +  '\033[1;31m if you would like to terminate this instance \033[1;m')
		time.sleep(1)

	def get_38(self):
		print('\033[1;41m Invalid option \033[1;m')
		time.sleep(2)

	def get_39(self):
		print ('\033[1;33m Exiting the menu  \033[1;m')
		time.sleep(2)
		print ('\033[1;34m Goodbye \033[1;m')
		time.sleep(1)
		sys.exit(2)

	def get_40(self):
		print('We will now install a sysstat on your instance')
		time.sleep(1)
		time.sleep(5)
		print('.')
		print('Just waiting for ssh port to open')
		time.sleep(5)
		print('..')
		time.sleep(5)
		print('...')
		time.sleep(5)
		print('....')

	def newline(self):
		print('\n')



