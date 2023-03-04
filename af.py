
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
 
def pascalUcgeni(yukseklik, satirlar=[]):
    satirlar.append([1])
    satir=[1]
    for i in range(yukseklik):
        sonraki = 0
        siradaki_satir = []
        for k in satir:
            siradaki_satir.append(sonraki + k)
            sonraki = k
        siradaki_satir.append(1)
        
        satir = siradaki_satir
        satirlar.append(satir)
    
    return satirlar
 
sayi = int(input("Pascal üçgeninin kaç satırını hesaplamak istiyorsunuz: "))
 
for x in pascalUcgeni(sayi):
    print(x)
 