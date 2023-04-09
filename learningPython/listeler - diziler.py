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
print(tumListeler[:2])
print(tumListeler[0:3])
print(tumListeler[2:])
print(tumListeler[1][3])
print(tumListeler[0][1:])