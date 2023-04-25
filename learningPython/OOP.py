# NESNE YONELIMLI PROGRAMLAMA

# 1 - class

import numpy as np
class test():
    print("bu bir sinif örnegi")

# --------------------------------------------------------

# class özellikleri


class calisanlar():
    bolum = ''
    sql = "evet"
    deneyim = 0
    bildigiDiller = []


# sınıfların özelliklerine erişmek
print(calisanlar.bolum)
print(calisanlar.sql)

# sınıfların özelliklerini değiştirmek
calisanlar.sql = "hayir"
print(calisanlar.sql)

# sınıf örneklendirmesi - o class'a ait nesneler oluşturma - class'ın özelliklerini taşır
ali = calisanlar()
print(ali.sql)
print(ali.deneyim)

# bu şekilde değiştirme yaptığımızda classta tanımlanan değer de değişir
ali.bildigiDiller.append("python")
print(ali.bildigiDiller)

veli = calisanlar()
print(veli.sql)

# classta tanımlanan değer değiştiği için "python" olarak çıktı verir
print(veli.bildigiDiller)

# aşağıda bunun çözümünün nasıl yapıldığı var

# --------------------------------------------------------


class calisanlar():
    def __init__(self):  # BURASI ONEMLI
        self.bildigiDiller = []


ali = calisanlar()
ali.bildigiDiller.append("python")
print(ali.bildigiDiller)

veli = calisanlar()
veli.bildigiDiller.append("java")
print(veli.bildigiDiller)

print(calisanlar().bildigiDiller)   # bunun boş dönmesinin sebebi classtaki değer direkt olarak değiştirmememiz

# --------------------------------------------------------


# üsttekinin devamı

class calisanlar():
    bildigiDiller = ["R", "Python"]     # class içinde genel tanımlama yaptık
    bolum = ""
    sql = ""
    deneyimYili = 0

    def __init__(self):                 # JAVADAKI CONSTRUCTOR MANTIGI
        self.bildigiDiller = []
        self.bolum = ""


ali = calisanlar()
ali.bildigiDiller.append("python")
ali.bolum = "end_muh"
print(ali.bildigiDiller)
print(ali.bolum)

veli = calisanlar()
veli.deneyimYili = 2
veli.bildigiDiller.append("java")
print(veli.bildigiDiller)
print(veli.deneyimYili)

print(calisanlar.bildigiDiller)

# --------------------------------------------------------


class veriBilimci():
    calisanlar = []

    def __init__(self):     # her veri bilimcinin kendine ait değiştirilebilir özelliğinin olması için burası lazım
        self.bildigiDiller = []
        self.bolum = ""

    def dilEkle(self, eklenecekDil):
        self.bildigiDiller.append(eklenecekDil)


ali = veriBilimci()
print(ali.bildigiDiller)
print(ali.bolum)

veli = veriBilimci()
print(veli.bildigiDiller)
print(veli.bolum)

ali.dilEkle("python")
print(ali.bildigiDiller)

veli.dilEkle("c++")
print(veli.bildigiDiller)

# --------------------------------------------------------

# miras yapıları (inheritance)


class employees():
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.address = ""


class dataScience(employees):       # parantez içinde referans olarak gönderince, employees() özellikleri miras alındı.
    def __init__(self):
        self.programming = ""


class marketing(employees):
    def __init__(self):
        self.storyTelling = ""


employee1 = dataScience()
employee1.firstName     # employee() özellikleri miras alındığı için firstName kullanabildik.

mar1 = marketing()
mar1.lastName           # employee() özellikleri miras alındığı için lastName kullanabildik.

# --------------------------------------------------------


# BASKA SEKILDE CLASS OLUSTURMA (MUHTEMELEN DAHA IYI)

class ogrenci(employees):
    def __init__(self, isim, no, tc):
        self.isim = isim
        self.no = no
        self.tc = tc


ali = ogrenci("ali", "11", "112233")
ali.address             # employee() özellikleri miras alındığı için lastName kullanabildik.

# --------------------------------------------------------


# vektörel operasyonlar
# OOP

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

print(ab)


# FP - functional programming


a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

print(a*b)
