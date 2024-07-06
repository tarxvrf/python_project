# python_project
semuanya tentang python
Saya coba membagi code yg dapat digunakan untuk mendeteksi SpecialChar '[@_!#$%^&*()<>?}{~:]', dimana kode ini dapat digunakan untuk mengamankan inputan dari user
codenya sebagai berikut:

import re 

karakter  = '[@_!#$%^&*()<>?}{~:]'
def cari(string):
   for data in string:
      regex= re.search(karakter,string)
      if not regex:
        pesan= "data tidak ditemukan"
      else:
          pesan="data ditemukan"
    return print(pesan)
cari("<script>")
