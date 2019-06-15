import ftplib
#import time

#host = '121.40.126.20'
host = 'localhost'
username = 'panll'
password = 'panll'

f = ftplib.FTP(host)
f.login(username, password)

#pwd_path = f.pwd()
#print('pwd_path: ', pwd_path)

def ftp_download():
    file_remote = 'mq_upload.py'
    file_local = '/root/mq_download.py'
    bufsize = 1024
    fp = open(file_local, 'wb')
    f.retrbinary('RETR %s' %file_remote, fp.write, bufsize)
    fp.close()

def ftp_upload():
    file_remote = 'mq_upload.py'
    file_local = '/root/mq.py'
    bufsize = 1024
    fp = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()

ftp_upload()
print('upload ok')
#time.sleep(2)
ftp_download()
print('download ok')
f.quit()
