# tuple
# sıralıdır, değiştirilemez

# üç şekilde de (satır 4-5-6) tuple oluşturulabilir
t = ("ali", "veli", 1, 2, 3, [4, 5, 6])
t = "ali", "veli", 1, 2, 3, [4, 5, 6]
t = ("test",)  # virgüle dikkat
print(type(t))

# --------------------------------------------------------

# dictionary - sozluk
# sırasız, değiştirilebilir
# listelerdeki gibi indexleme yapılamaz

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk = {"REG": 10,
          "LOJ": 20,
          "CART": 30}

sozluk = {"REG": ["RMSE", 10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE", 30]}

print(sozluk)

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

# print(sozluk[0]) # bu şekilde çalışmaz çünkü indexleme yapılamaz, elemana erişebilmek için aşağıdaki gibi kullan
print(sozluk["REG"])
print(sozluk["CART"])

# --------------------------------------------------------

sozluk = {"REG": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},

          "LOJ": {"RMSE": 10,
                  "MSE": 20,
                  "SSE": 30},        # sözlük içinde sözlük şeklinde de olabilir.

          "CART": {"RMSE": 10,
                   "MSE": 20,
                   "SSE": 30},
          }

print(sozluk["REG"]["SSE"])

# --------------------------------------------------------

# sözlük yapısında elemen ekleme ve değiştirme

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"  # burda eleman eklendi
print(sozluk)

sozluk["REG"] = "Coklu Dogrusal Regresyon"  # burda eleman değiştirdik
print(sozluk)

# "1: Yapay Sinir Aglari" olarak yeni sözlük elemanı eklendi
sozluk[1] = "Yapay Sinir Aglari"
print(sozluk)

yeniTuple = ("tuple",)
sozluk[yeniTuple] = "yeni bir tuple"
print(sozluk)

# --------------------------------------------------------

# setler - kümeler oluşturma
# sırasızdır
# tekrar eden değerler yoktur

yeniListe = [1, "s", "ali", 123]
yeniSet = set(yeniListe)                # liste ile yeni set oluşturduk
print(yeniSet)

t = ("a", "ali")
yeniSet = set(t)                # tuple ile yeni set oluşturduk
print(yeniSet)

ali = "lutfen_ata_ba kma_u zaya_git"
yeniSet = set(ali)
print(yeniSet)

liste = ["lutfen", "ata", "bakma", "uzaya", "git", "ali", "ali", "git"]
yeniSet = set(liste)
print(yeniSet)

# --------------------------------------------------------

# set-küme eleman ekleme çıkarma

liste = ["gelecegi", "yazanlar"]
s = set(liste)

s.add("ile")
s.add("gelecege_git")
print(s)

# remove ile silerken, silmeye çalıştığımız eleman set içinde yoksa hata verir
s.remove("ile")
print(s)                # programın akışı durur.

# discard ile silme işlemi yaptığımızda, silmek istediğimiz eleman set içinde yoksa
s.discard("gelecege_git")
print(s)                        # bile uyarı vermeden devam eder.


# --------------------------------------------------------

# setlerde klasik küme işlemleri

# difference

set1 = {1, 3, 5}
set2 = {1, 2, 3}

ikiKumeFarki = set1.difference(set2)    # set1'de olup set2'de olmayanlar
print(ikiKumeFarki)

ikiKumeFarki = set2.difference(set1)    # set2'de olup set1'de olmayanlar
print(ikiKumeFarki)

farkliliklar = set1.symmetric_difference(set2)  # ikisinde de ortak olmayanlar
print(farkliliklar)
# aynı işlem set1 - set2 veya set2 - set1 şeklinde de yapılabilir.

# --------------------------------------------------------

# setlerde kesişim (intersection) ve birleşim (union)

set1 = {1, 3, 5}
set2 = {1, 2, 3}

kesisim = set1.intersection(set2)          # kesişim işlemi yapıldı
print(kesisim)

# üstteki metot ile kesişim alır ama bu şekilde de kesişim alabilir,z
kesisim2 = set1 & set2
print(kesisim2)

birlesim = set1.union(set2)
print(birlesim)

x = set1.intersection_update(set2)      # bunu tam anlamadım
print(x)

# --------------------------------------------------------

# setlerde sorgu işlemleri

set1 = {4, 13, 76}
set2 = {3, 4, 76, 5, 13, 11}

# iki kümenin kesişiminin boş olup olmadığının sorgulanması
a = set1.isdisjoint(set2)
print(a)

# bir kümenin elemanlarının başka bir küme içerisinde yer alıp almadığının kontrolü - alt kümesi midir mevzusu
x = set1.issubset(set2)
print(x)

# bir kümenin diğer kümeyi kapsayıp kapsamadığının kontrolü
y = set2.issuperset(set1)
print(y)

