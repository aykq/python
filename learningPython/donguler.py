isimler = ["ahmet", "burak", "mehmet", "ugur", "a", "b", "z"]

for degisken in isimler:
    print(degisken)

for i in range(10):
    print(i)

print("\n")

for i in range(len(isimler)):
    print(i)

print("\n")

for i in range(len(isimler)):
    print(isimler[i])

for i in range(10):
    print(i)

for i in range(3, 10):  # başlangıç 3, bitiş 9. 10 dahil değil.
    print(i)

for i in range(2, 31, 2):  # başlangıç 2, bitiş 31. 2 arttırarak say.
    print(i)


# --------------------------------------------------------

# dongu ve fonksiyonu beraber kullanmak
# maaslara %20 zam yapilacak

maaslar = [1000, 2000, 3000, 4000]


def zamliMaas(x):
    print(x*20/100 + x)

# zamliMaas(2000)


for i in maaslar:
    print(zamliMaas(i))

# --------------------------------------------------------

# if, for ve fonksiyonları bir arada kullanmak
# maas > 3000 - %10 zam
# maas < 3000 - %20 zam

maaslar = [1000, 2000, 3000, 4000, 5000]


def yuzdeOn(x):
    print(x*10/100 + x)


def yuzdeYirmi(x):
    print(x*20/100 + x)


for i in maaslar:
    if i >= 3000:
        yuzdeOn(i)

    else:
        yuzdeYirmi(i)

# --------------------------------------------------------

# break ve continue

maaslar = [8000, 5000, 2000, 1000, 3000, 7000, 1000]
maaslar.sort()
print(maaslar)

for i in maaslar:       # break kullanımı
    if i == 3000:
        print("donguden cikildi")
        break
    
    else:
        print(i)
    
    
for i in maaslar:       # continue kullanımı
    if i == 3000:
        print(str(i) + " degeri atlandi")
        continue
    
    else:
        print(i)
    
# --------------------------------------------------------

# while

sayi = 0
while sayi < 10:
    sayi += 1
    print(sayi)