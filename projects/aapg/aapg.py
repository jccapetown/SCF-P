#File Name   : aapg.py 
#Description : aapg 
#Author      : Jacques Coetzee 
#Date        : 2016-06-21 08:34:12.758000 


#Import Section
import os,sys,datetime
sys.path.append('../../includes') 
#import func_file
#import func_strings
import func_ftp
import func_inifile


#Global Variables
ftpserver = '127.0.0.1'
ftpusername = 'username'
ftppassword = 'password'
ftpfilepath = '/'

server_gameini = 'aagame.ini'
server_gameini_dst = 'serverconfig/aagame.ini'
my_ini = 'myconfig/aagame.ini'
new_gameini = 'generatedconfig/aagame.ini'
backupfile = '%s_%s' % (server_gameini, datetime.date.today().strftime('%d%b%Y') )
#Function/Methods/class definition



#Main Section

#Download the original config file
ftp = func_ftp.connect(ftpserver, ftpusername, ftppassword)
func_ftp.cd(ftp,ftpfilepath) 
#files = func_ftp.lst(ftp)
func_ftp.download(ftp, server_gameini,server_gameini_dst)
func_ftp.close(ftp)

#Open the original file and load the config
f = open(server_gameini_dst,'rb')
serverfile = f.readlines()
f.close()

#sort the file into a dictionary
filedict = {}
func_inifile.get_dict(filedict, serverfile)
            

#Open my config file and load the config
f = open(my_ini,'rb')
myfile = f.readlines()
f.close()
#sort the my config file into a dictionary
myfiledict = {}
func_inifile.get_dict(myfiledict, myfile)

#Now go through my config and update the serverdict
for section in myfiledict:
    for key in myfiledict[section]:

        if section in filedict:
            if key in filedict[section]:
                filedict[section][key] = []
        
                for val in myfiledict[section][key]:
                    filedict[section][key].append(val)

#write the new ini file
func_inifile.write_ini(new_gameini,filedict) 

               
#Rename the ftp server config file and copy the new one
ftp = func_ftp.connect(ftpserver, ftpusername, ftppassword)
func_ftp.rename(ftp, server_gameini, backupfile)
func_ftp.upload(ftp, new_gameini, server_gameini)
func_ftp.close(ftp)                
            
    









