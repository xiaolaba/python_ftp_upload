# by xiaolaba, port to python 3.7.3
# 2020-AUG-11
#   print string, change to print (string)
#   raw_input, change to input
#   all SPACE for indentation
# tested, ls command is ok

## copy here https://gist.github.com/Nemolog/72475/8b19af5a27cfe03e90601bf523297734c24086e4
## change some code to uses with python 3.7.3


host = "ftp.server.com"
login = "user name"
psw = "password"
directory = "temp_folder"


import ftplib, sys, os

def command():
  cmd = input(login +"@" + host +">")
  ### upload
  if cmd=="upload": 
    #filename = input("Insert file name:")
    filename = "1.pdf"
    path = os.path.abspath('') + "\\"   #current working directory path
    path = path.replace("\\","\\\\")    # format path with \\ escape char
    print ('full path =', path )
    print (path + "\r\n")       
 
    ### Upload a binary file from your disk
    #ftp.storbinary('STOR '+filename, open(filename,'rb'))
    ftp.storbinary('STOR '+ filename, open( path + filename,'rb'))    
    print ("file upload success!")
 
    command()

  #download
  if cmd=="download":
    filenameHost = input("Insert file name (on server):")
    filename = input("Insert file name (in your disk):")
    ftp.retrbinary('RETR '+filenameHost, open(filename,'wb').write)
    print ("file download success!")

    command()

  if cmd=="cd":
    newDir = input("new dir:")
    ftp.cwd(newDir)

    print (ftp.retrlines("LIST"))
    command()

  #help
  if cmd=="help":
    print ("-------------------------------------------------")
    print (".:[ ByteZoneFtp Help ]:."                         )
    print (""                                                 )
    print ("Aviable commands:"                                )
    print ("- upload (upload files from your disk to server)" )
    print ("- download (download files from server)"          )
    print ("- cd (change directory)"                          )
    print ("- quit"                                           )
    print ("-------------------------------------------------")
    command()

  #quit
  if cmd=="quit": 
    print ("quit from " + host             )
    print ("------------------------------")
    print ("ByteZoneFtp v0.1 Beta"         )
    print ("by Nemolog"                    )
    print (""                              )
    print ("follow me http://plumfake.net" )
    print ("------------------------------")
    ftp.quit()
    exit()

  else:command()

print ("------------------------------")
print ("Wellcome ByteZoneFtp v0.1 Beta")
print ("by Nemolog"                    )
print (""                              )
print ("follow me http://plumfake.net" )
print ("------------------------------")

#host = input("Insert Host:")
#login = input("Insert Login:")
#psw = input("Insert Password:")
#directory = input("Insert direcory (default '/'):")

if directory == "": directory = "/"

print ("try connect to " + login +":*******@" + host )

try: ftp = ftplib.FTP(host)
except ftp.all_errors as error:
    print("Cannot connect:", error)
else:
    try: ftp.login(login, psw)
    except ftp.all_errors as error:
        print("Cannot login:", error)
    else:

        print(ftp.getwelcome())
        #ftp.cwd(directory)

        ftp.cwd(directory) #Change Working Directory
        wdir2 = ftp.pwd()           #get Path of Working Directory
        print("\r\nChange to Dir: " + wdir2 + "\r\n") #show Path of Working Directory
        print ("\r\n listing this Dir: \r\n" + ftp.retrlines("LIST"))  # show file names of Working Directory

        ftp.dir('1.txt')
        
        #ftp.quit()
        
        #input('\r\nJob Done. byebye')
        
        #print(ftp.retrlines("LIST"))
        
        path = os.path.abspath('') + "\\"   #current working directory path
        path = path.replace("\\","\\\\")    # format path with \\ escape char
        print ('full path =', path )
        print (path + "\r\n")   
        
        command()