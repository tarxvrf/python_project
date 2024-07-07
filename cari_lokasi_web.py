############CarilokasiWeb#####
inputan= input('masukan web =')
ip= socket.gethostbyname(inputan)
url='https://geolocation-db.com/jsonp/'+ip
respons= requests.get(url)
geo= respons.content.decode()
geos= geo.split('(')[1].strip(')')
geok= json.loads(geos)
for k,v in geok.items():
    print(f'{k} : {v}')
#######Cari lokasi Web#######