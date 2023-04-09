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