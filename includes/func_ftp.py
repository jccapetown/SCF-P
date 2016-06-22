import ftplib

def connect(host, uname, pword):
    try:
        ftp = ftplib.FTP(host,uname, pword)
        return ftp
    except:
        return None

def close(ftpObj):
    try:
        ftpObj.quit()
        return True
    except:
        return False

def lst(ftpObj):
    try:
        data = ftpObj.nlst()
        return data
    except:
        return False

def cd(ftpObj, directory):
    try:
        #ftpObj.cwd('/pub/')
        ftpObj.cwd(directory)
        return True
    except:
        return False

def download(ftpObj, filename, dstfilename):
    try:
        ftpObj.retrbinary("RETR " + filename ,open(dstfilename, 'wb').write)
        return True
    except:
        return False


def upload(ftpObj, filename, dstfilename):
    try:
        import os
        ext = os.path.splitext(filename)[1]
        if ext in (".txt", ".htm", ".html"):
            ftpObj.storlines("STOR " + dstfilename, open(filename))
        else:
            ftpObj.storbinary("STOR " + dstfilename, open(filename, "rb"), 1024)
        return True
    except Exception, e:
        return False

def rename(ftpObj, fromname, toname):
    try:
        ftpObj.rename(fromname, toname)
        return True
    except:
        return False
    
    
