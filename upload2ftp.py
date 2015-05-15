#!/usr/bin/python
############################
# Python script >= 2.7
# Author : Mickael Menard
# Date : 2015/05/15
# version: 0.2
#
# Send files given in argument to a FTP server
# You must configure username, password, ftp server in ftpconf.ini file
#
# usage:
#      python upload2ftp ./test.png
#      python upload2ftp ./test.png ../foo/another_test.jpg
#      python upload2ftp ./*.png
#
############################
version = '0.2'

import sys
if sys.version_info < (2,7):
  sys.stderr.write("This script requires Python 2.7 or newer.\n")
  sys.stderr.write("Current version: " + sys.version + "\n")
  sys.stderr.flush()
  sys.exit(1)
import os, shutil
import ftplib


# Local global variables
AUTOMATOR = 0


if AUTOMATOR==0:
	## Read Config from config.ini file
	import ConfigParser
	config = ConfigParser.ConfigParser()
	try:
		config.read(os.path.join(os.path.dirname(sys.argv[0]), "ftpconfdefault.ini"))
		#config.read(os.path.join(os.path.dirname(sys.argv[0]), "../../Python/upload2ftp/ftpconf.ini"))
		FTP_USERNAME = eval(config.get('Config','FTP_USERNAME'))
		FTP_PWD = eval(config.get('Config','FTP_PWD'))
		FTP_SERVER = eval(config.get('Config','FTP_SERVER'))
		FTP_OUT_DIR = eval(config.get('Config','FTP_OUT_DIR'))
		FTP_DEBUG = eval(config.get('Config','FTP_DEBUG'))
		DEBUG = eval(config.get('Config','DEBUG'))
		CUSTOM_SERVICE = eval(config.get('Config','CUSTOM_SERVICE'))
	except:
		print "Error occured during opening configuration file"
		sys.exit(1)
else:
	## Local definitions
	DEBUG=1
	FTP_USERNAME=''
	FTP_PWD=''
	FTP_SERVER=''
	FTP_OUT_DIR=''
	FTP_DEBUG=0
	CUSTOM_SERVICE=''

	
##
## Print custom info
##
if DEBUG!=0:
	print "DEBUG: FTP_SERVER = %s" % FTP_SERVER
	print "DEBUG: FTP_OUT_DIR = %s" % FTP_OUT_DIR
	print "DEBUG: FTP_USERNAME = %s" % FTP_USERNAME
	print "DEBUG: FTP_PWD = %s" % FTP_PWD
	print "DEBUG: FTP_DEBUG = %s" % FTP_DEBUG
	print "DEBUG: CUSTOM_SERVICE = %s" % CUSTOM_SERVICE
	#print "DEBUG = %s" % DEBUG


def handle(block):
    #f.write(block)
    print ".", 
    
def main():
	nb_files_transfered = 0
	print "%s FTP uploder v%s" % (CUSTOM_SERVICE, version)
	# Debug, current location
	#print os.getcwd()

	if len(sys.argv) == 1:
		print "No input file(s)"
		sys.exit()
	else:
		print "%d file(s) to be sent..." % (len(sys.argv)-1)
		ftp = ftplib.FTP() 
		ftp.set_debuglevel(FTP_DEBUG)
		if len(FTP_SERVER)==0:
			print "Please update the configuration file, server not found!"
			sys.exit(1)
		print "Logging in..." 
		try:
			ftp.connect(FTP_SERVER) 
		except:
			print "ERR: connection to %s failed" % FTP_SERVER
		print ftp.getwelcome()
		ftp.login(FTP_USERNAME, FTP_PWD)
		if DEBUG!=0:
			print "DEBUG: current dir = %s" % ftp.pwd()

	# For each file
	for file_in in sys.argv[1:]:
		folder, base = os.path.split(file_in)
		if DEBUG!=0:
			print file_in
			print "DEBUG: folder = %s" % folder
			print "DEBUG: base = %s" % base

		try:
			file = open(file_in, "rb")
		except:
			print "ERR: opening file %s, file skipped" % file_in
			continue

		# FTP Sub dir creation
		if len(FTP_OUT_DIR) > 0:
			if DEBUG!=0:
				print "Creating %s on server %s" % (FTP_OUT_DIR, FTP_SERVER)
			ftp.mkd(FTP_OUT_DIR)
			ftp.cwd(FTP_OUT_DIR)

		# Move to local folder
		os.chdir(folder)

		#print 'STOR ' + base
		try:
			print "STORing File %s now..." % base
			#ftp.storbinary('STOR ' + base, file, callback=handle, blocksize=4096) 
			ftp.storbinary('STOR ' + base, file) 
			nb_files_transfered = nb_files_transfered + 1
		except:
			try:
				ftp.quit()
			except:
				ftp.close()
			ftp.connect(server)
			try:
				print "STORing File %s again..." % base
				#ftp.storbinary('STOR ' + base, file, callback=handle, blocksize=4096) 
				ftp.storbinary('STOR ' + base, file) 
				nb_files_transfered = nb_files_transfered + 1 # assuming
				file.close()
				print "File transfered" 
			except:
				file.close()
				print "ERR: File NOT transfered!" 
	try:
		ftp.quit()
	except:
		ftp.close()

	#if (len(sys.argv)-1) == 1:
	if nb_files_transfered == 1:
		#print "%d file has been transfered" % (len(sys.argv)-1)
		print "%d file has been transfered" % nb_files_transfered
	else:
		#print "%d files have been transfered" % (len(sys.argv)-1)
		print "%d files have been transfered" % nb_files_transfered
 

# Entry point
if __name__ == "__main__":
	main()