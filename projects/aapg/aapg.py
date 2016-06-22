#File Name   : aapg.py 
#Description : This script remotely updates Americas Army Proving Grounds config files with your prefered config 
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
ftpserver = 'server'
ftpusername = 'usern'
ftppassword = 'password'
ftpfilepath = '/1223840/aapg/AAGame/Config/'

server_gameini = 'AAGame.ini'
server_gameini_dst = 'serverconfig/AAGame.ini'
my_ini = 'myconfig/AAGame.ini'
new_gameini = 'generatedconfig/AAGame.ini'

server_UGCfile = 'AASteamUGCManager.ini'
server_UGCfile_dst = 'serverconfig/AASteamUGCManager.ini'
my_UGCfile = 'myconfig/AASteamUGCManager.ini'


server_pbfile = 'pbsvuser.cfg'
server_pbfile_dst = 'serverconfig/pbsvuser.cfg'
my_pbfile = 'myconfig/pbsvuser.cfg'
pbpath = '/1223840/aapg/Binaries/Win32/pb'


backupdate = datetime.date.today().strftime('%d%b%Y')
backupfile = '%s_%s' % (server_gameini, backupdate )
backupUGCfile = '%s_%s' % (server_UGCfile, backupdate )
backupPBfile = '%s_%s' % (server_pbfile, backupdate )




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
func_ftp.cd(ftp,ftpfilepath) 
func_ftp.rename(ftp, server_gameini, backupfile)
func_ftp.upload(ftp, new_gameini, server_gameini)
func_ftp.close(ftp)                
            
    
#Lets check the UGC file
ftp = func_ftp.connect(ftpserver, ftpusername, ftppassword)
func_ftp.cd(ftp,ftpfilepath) 
func_ftp.download(ftp, server_UGCfile,server_UGCfile_dst)
func_ftp.rename(ftp, server_UGCfile, backupUGCfile)
func_ftp.upload(ftp, my_UGCfile, server_UGCfile)
func_ftp.close(ftp)



#Lets check the PBSV file
ftp = func_ftp.connect(ftpserver, ftpusername, ftppassword)
func_ftp.cd(ftp,pbpath) 
func_ftp.download(ftp, server_pbfile,server_pbfile_dst)
func_ftp.rename(ftp, server_pbfile, backupPBfile)
func_ftp.upload(ftp, my_pbfile, server_pbfile)
func_ftp.close(ftp)





