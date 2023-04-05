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

# strip() - karakter kırpma

