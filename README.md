upload2ftp
==========

Author : 
	Mickaël Ménard

Purpose:
	Upload files to a FTP server.

Features:
    Uploads one or several files gave in argument to a FTP server
	Authentification supported
	If the file exist it is OVERWRITTEN.

THIS SCRIPT IS PROVIDED WITH NO WARRANTY WHATSOEVER. PLEASE REVIEW THE SOURCE CODE TO MAKE SURE IT WILL WORK FOR YOUR NEEDS. IF YOU FIND A BUG, PLEASE REPORT IT.

Requirements:
    Python 2.7+

Setup:
	Customize ftpconf.ini with at least the server address. username and password would be needed too.
	Place the file upload.py and ftpconf.ini in any directory and run (execution privs required):

	$ ./upload2ftp.py
	or
	$ python upload2ftp.py

Q&A:
    Q: Who is this script designed for?
    A: Those people comfortable with the command line that want to backup their media on a FTP server. Personnally I use it to upload my photo I want to share.
    
    Q: Is it well coded
    A: Not so much but it does what I need :)

    Q: Is this script feature complete and fully tested?
    A: Yep.

History:
	- V0.1 : internal use
	- V0.2 : First GitHub version
