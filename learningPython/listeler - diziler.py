# [] veya list() kullanarak liste oluşturulabilir

isimler = ["ahmet", "burak", "mehmet", "ugur"]

print(isimler)
print(isimler[0])
print(isimler[1])
print(isimler[2])

print (len(isimler))
print(type(isimler))

isimler = ["ahmet", "burak", "mehmet", "ugur"]
isimler2 = ["fatma", "ayse", "mahmut", "oguz"]

yeniListe = ["a", 19.2, 30, isimler2]
print(type(yeniListe))
print(type(yeniListe[0]))
print(type(yeniListe[1]))
print(type(yeniListe[2]))
print(type(yeniListe[3]))

tumListeler = [isimler, isimler2, "aa", "12.2", 12]
print(tumListeler[:2]) # dizinin başında 2. indexteki elemana kadar
print(tumListeler[0:3]) # 0. indexteki elemandan 3. indexteki elemana kadar
print(tumListeler[2:]) # 2. indexteki elemandan dizinin sonuna kadar
print(tumListeler[1][3]) # dizinin 1. indexinde bulunan dizi elemanının içindeki 3. indexteki eleman
print(tumListeler[0][1:]) # dizinin içindeki dizinin elemanına erişmek

#--------------------------------------------------------

# metotlar ile eleman ekleme, silme - append(), remove()

isimler3 = ["ali", "veli", "berk", "deniz", "ayse"]
print(isimler3)
 
isimler3.append("armut")
print(isimler3)

isimler3.remove(isimler3[0])
isimler3.remove("berk")
print(isimler3)

#--------------------------------------------------------

# indexe göre eleman ekleme, silme - insert(), pop()

isim4 = ["ali", "veli", "berk", "deniz", "ayse"]
isim4.insert(1, "test") # 1. indexe "test" elemanını ekle
print(isim4)
isim4.insert(len(isim4), "beren")
print(isim4)

isim4.pop(0)
print(isim4)

#--------------------------------------------------------

# diger liste metotları

isimler = ["ahmet", "burak", "mehmet", "ugur"]
isimler2 = ["fatma", "ayse", "mahmut", "oguz"]
isimler3 = ["ali", "veli", "berk", "deniz", "ayse"]
isim4 = ["ali", "veli", "berk", "deniz", "ayse"]

liste = isimler + isimler2 + isimler3 + isim4
print(liste)

print(liste.count("ayse"))
print(liste.count("mehmet"))


