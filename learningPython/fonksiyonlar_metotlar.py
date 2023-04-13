def isimleriListele():
    isimler = ["ahmet", "burak", "mehmet", "ugur", "a", "b", "z"]
    for i in range(len(isimler)):
        print(isimler[i])


isimleriListele()

# --------------------------------------------------------

def kareAl(x):
    print("girilen " + str(x) + " sayisinin karesi: " + str(x**2))

kareAl(5)

# --------------------------------------------------------

# 2 argümanlı fonksiyon
def carpma(x, y):
    print("sonuc: " + str(x*y))

carpma(3, 5)

# --------------------------------------------------------

# 2 argümanlı fonksiyon - return ile
def carpma(x, y):
    return x*y

cikti = carpma(3, 5)
print(cikti)

# --------------------------------------------------------

# local ve global değişkenler
x = 20
y = 30      # bunlar global değişken

def carp(x, y):     # metot parametresi olarak verilen değişkenlerveya döngü değişkenleri local değişkendir
    print(x*y)

# --------------------------------------------------------

# local ==>> global değişken

x = []      # global olan değişken

def elemanEkle(y):      # tanımlanan metot içerisinde x diye bir değişken olmadığı için x değişkenini global olarak
    x.append(y)         # aramaya başlar ve değiştirir. yani metot içerisinde tanımladığımız x local değişkeni, 
                        # global olan x değişkenine etki eder.
    print(str(y) + " ifadesi eklendi")
    print(x)
    
elemanEkle(3)
elemanEkle(2)
elemanEkle("ali")

