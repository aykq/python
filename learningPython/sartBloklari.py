sayi1 = 5
sayi2 = 5

if sayi1 > sayi2:
    print("birinci sayi daha buyuk - " + sayi1)


elif sayi1 < sayi2:
    print("ikinci sayi daha buyuk - " + sayi2)


else:
    print("sayilar esit")

# --------------------------------------------------------

sinir = 50000
magazaAdi = input("magaza adi nedir?")
gelir = int(input("magazanin geliri: "))

if gelir > sinir:
    print("gelir, sinirdan yuksek")

elif gelir < sinir:
    print("gelir, sinirdan dusuk")

else:
    print("gelir, sinir deger ile ayni")
