import math
#1
def toplama(a,b):
    return a+b
#2
def cıkarma(a,b):
    return a-b
#3
def carpma(a,b):
    return a*b
#4
def bolme(a,b):
    return a/b
#5
def usalma(a,b):
    return a**b
    
print("****Hesap Makinesi İşlemleri****")
print("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Üs Alma\n6-Logaritma\n7-Karekök\n8-Sin\n9-Çıkış")
secim=int(input("Yapmak İstediğiniz İşlemi Seçin: "))
while True:
    if(secim==9):
        print("Çıkış Yaptınız..Hoşçakalın...")
        break
    elif(secim==1):
        a=int(input("1.Sayıyı Girin:"))
        b=int(input("2.Sayıyı Girin:"))
        print(toplama(a,b))

    elif(secim==2):
        a=int(input("1.Sayıyı Girin:"))
        b=int(input("2.Sayıyı Girin:"))
        print(cıkarma(a,b))

    elif(secim==3):
        a=int(input("1.Sayıyı Girin:"))
        b=int(input("2.Sayıyı Girin:"))
        print(carpma(a,b))

    elif(secim==4):
        a=int(input("1.Sayıyı Girin:"))
        b=int(input("2.Sayıyı Girin:"))
        print(bolme(a,b))

    elif(secim==5):
        a=int(input("1.Sayıyı Girin:"))
        b=int(input("2.Sayıyı Girin:"))
        print(usalma(a,b))
         
    elif(secim==6):
        logaritma=float(input("Logaritmasını istediğiniz sayıyı girin: "))
        logu=math.log10(logaritma)
        print(logu)

    elif(secim==7):
        a=float(input("Karekökünü almak istediğiniz sayıyı girin: "))
        karekök=math.sqrt(a)
        print(karekök)

    elif(secim==8):
        a=float(input("Sinüsünü almak istediğiniz sayıyı girin: "))
        sinüs=math.sin(a)
        print(sinüs)
        

    






