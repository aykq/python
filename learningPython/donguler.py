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
