str = "bi kac kelimelik string"
print(len(str))


# upper() - büyük harf

print(str.upper())
print(str.isupper())
buyukYazdir = str.upper()
buyukMu = str.isupper()
print(buyukYazdir)
print(buyukMu)


# lower() - küçük harf

print(str.lower())
print(str.islower())
kucukYazdir = str.lower()
kucukMu = str.islower()
print(kucukYazdir)
print(kucukMu)
# print("kucuk harfli mi? " + str(kucukMu))
print(str)

#--------------------------------------------------------

# replace() - harf değiştirme

str.replace("k", "n")
print(str.replace("k", "n"))

#--------------------------------------------------------

# strip() - karakter silme (sadece strip() kullanıldığında sondaki veya baştaki boşlukları siler)
# strip("-buraya istediğin harfi gir-") şeklinde kullandığında, yazdığın harfi baştan ve sondan siler

str2 = "   bi kac kelimelik string a  "
yeniStr = str2.strip()
print(str2)
print(yeniStr)

str2 = "qbi kac kelimelik stringq"
yeniStr2 = str2.strip("q")
print(yeniStr2)

#--------------------------------------------------------

# substring - verilen stringin belirtilen indexindeki değeri yazdırma

str3 = "bi kac kelimelik string"
print(str3[0])
print(str3[0:6])