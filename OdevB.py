file=open("Kutuphane.txt","w",encoding="utf-8")
print(file)

file.write("Köle Olmayacağız,Aliya, Tarih \nVar Mısın,Doğan Cüceloğlu,Kişisel Gelişim \nYakın Tarihin Gerçekleri,İlber Ortaylı,Tarih \nİnsan Olmak,Engin Gençtan,Kişisel Gelişim \nSimyacı,Paulo Coelho,Kişisel Gelişim\nMalcolm X, Malcolm X, Tarih\n ")
print()
file=open("Kutuphane.txt","r",encoding="utf-8")

dosya=file.read()
print(dosya)

file2=open("tarih.txt","w",encoding="utf-8")
print(file2)

file2.write("Köle Olmayacağız,Aliya, \nYakın Tarihin Gerçekleri,İlber Ortaylı \nMalcolm X, Malcolm X")
print()

file3=open("kisiselgelisim.txt","w",encoding="utf-8")
print(file3)

file3.write("Var Mısın,Doğan Cüceloğlu, \nİnsan Olmak,Engin Gençtan, \nSimyacı,Paulo Coelho")