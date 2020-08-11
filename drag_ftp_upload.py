server = 'ftp.server.name'
username = 'user name'
password = 'password'
remote_folder = 'temp_dir'

# python 3.7.3, win10, test done
# by xiaolaba, 2019-JAN-10
# user drag & drop a file to this python script, the file will upload to ftp/remote_foler
# command line is no longer working, only for debug purpose

import ftplib
import os, sys

path = os.path.abspath('') + "\\"   #current working directory
print ('os.path.abspath = ' + path)

droppedFile = sys.argv[1]            # user drag and drop the file for upload
droppedFile = droppedFile.replace(path,"")    # remove path string
print ("dropfile name = " + droppedFile)

path = path.replace("\\","\\\\")    # format path with \\ escape char
print ('full path name for open file = ', path + "\r\n" )

print ("login ftp now\r\n" )
ftp=ftplib.FTP(server)

print(ftp.getwelcome())

ftp.login(username, password)
login_response = ftp.login(username, password)
print(login_response)

#ftp = ftplib.FTP(server, username ,paswwrod)

print("\r\nUploading to " + server + "/" + remote_folder + "/\r\n")  # show file names of Working Directory

#input('ready ? press ENTER to go')

#ftp.dir('1.txt')
#ftp.dir('2.txt')

ftp.dir(droppedFile)

#wdir = ftp.pwd()
#print(wdir)
#print (ftp.retrlines("LIST"))  # show root files listing

ftp.cwd(remote_folder) #Change Working Directory
#wdir2 = ftp.pwd()     #get Path of ftp Working Directory
#print(wdir2)          #show Path of ftp Working Directory
#print (ftp.retrlines("LIST"))  # show file listing of Working Directory

#file = open('C:\\Users\\user0\\Desktop\\temp\\ftp_upload\\1.txt','rb') # local file to send
#file = open(path + dropfile,'rb') # local file to send

#ftp.storbinary('STOR 1.txt', file)     # send the file, binary mode
#ftp.storbinary('STOR ' + dropfile, file)     # send the file, binary mode

ftp.storbinary('STOR '+ droppedFile, open( path + droppedFile,'rb'))

print("\r\nUpload done, login FTP to see the archive as following,\r\n")

#ftp.dir('1.txt')
ftp.dir(droppedFile)    # show the file upload

#ftp.quit()

input('\r\nDone. byebye')
