import numpy as np
import pandas as pd

Arr=np.array([[50,12,np.nan,16],[np.nan, np.nan,80,70],[93,np.nan,16,np.nan]])
df=pd.DataFrame(Arr, index=["1.Satır","2.Satır","3.Satır"],columns=["1.Sütun","2.Sütun","3.Sütun","4.Sütun"])
print(df)
print()
print("Bilinen Verilerin toplamı ↓↓")
print(df.sum().sum())
print("Toplam veri sayısı ↓↓")
print(df.size)
print("Bilinmeyen veri sayısı ↓↓")
print(df.isnull().sum().sum())

def ortalamaBul(df):
    toplamDeger=df.sum().sum()
    toplamSayi=df.size-df.isnull().sum().sum()
    return toplamDeger/toplamSayi

print(df.fillna(value=ortalamaBul(df),inplace=False))





















""" #a=np.arange(1,17).reshape(4,4)
#print(a)
print("\n")
#4x3’lük rasgele sayılardan oluşturan bir DataFrame oluşturun. Sütun ve index isimlerini istediğiniz gibi verebilirsiniz
print("C Maddesi-->2.Ödev")

from numpy.random import randn

b=df = pd.DataFrame(data = randn(4,3), index = ['1.Satır','2.Satır','3.Satır','4.Satır'], columns = ['Sütun->1','Sütun->2','Sütun->3'])
print(b)

#Arr=np.array([[50,12,np.nan,16],[np.nan, np.nan,80,70],[93,np.nan,16,np.nan]]) değerlerinden oluşan array’i DataFrame’e çevirin. 
#Kayıp değerler (missing value) ile ilgili neler yapılabilir uygulayın. (Ortalama değer alıp kayıp değerlere yazabilirsiniz).
print("\n")
print("C Maddesi-->3.Ödev")
Arr=np.array([[50,12,np.nan,16],[np.nan, np.nan,80,70],[93,np.nan,16,np.nan]])
df=pd.DataFrame(Arr, index=["1.Satır","2.Satır","3.Satır"],columns=["1.Sütun","2.Sütun","3.Sütun","4.Sütun"])
print(df)

print(df.sum().sum())
print(df.size)
print(df.isnull().sum().sum())

def ortalamaBul(df):
    toplamDeger=df.sum().sum()
    toplamSayi=df.size-df.isnull().sum().sum()
    return toplamDeger/toplamSayi

print(df.fillna(value=ortalamaBul(df),inplace=False))


 """