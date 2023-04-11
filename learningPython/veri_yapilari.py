# tuple
# sıralıdır, değiştirilemez

t = ("ali", "veli", 1, 2, 3, [4, 5, 6]) # üç şekilde de (satır 4-5-6) tuple oluşturulabilir
t = "ali", "veli", 1, 2, 3, [4, 5, 6]
t = ("test",)  # virgüle dikkat
print(type(t))

#--------------------------------------------------------

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

#--------------------------------------------------------

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

#--------------------------------------------------------

# sözlük yapısında elemen ekleme ve değiştirme

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"  # burda eleman eklendi
print(sozluk)

sozluk["REG"] = "Coklu Dogrusal Regresyon"  # burda eleman değiştirdik
print(sozluk)

sozluk[1] = "Yapay Sinir Aglari"  # "1: Yapay Sinir Aglari" olarak yeni sözlük elemanı eklendi
print(sozluk)

yeniTuple = ("tuple",)
sozluk[yeniTuple] = "yeni bir tuple"
print(sozluk)

#--------------------------------------------------------

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

#--------------------------------------------------------

# set-küme eleman ekleme çıkarma

liste = ["gelecegi", "yazanlar"]
s = set(liste)

s.add("ile")
s.add("gelecege_git")
print(s)

s.remove("ile")         # remove ile silerken, silmeye çalıştığımız eleman set içinde yoksa hata verir
print(s)                # programın akışı durur.

s.discard("gelecege_git")       # discard ile silme işlemi yaptığımızda, silmek istediğimiz eleman set içinde yoksa
print(s)                        # bile uyarı vermeden devam eder.


#--------------------------------------------------------

# setlerde klasik küme işlemleri

#difference

set1 = {1, 3, 5}
set2 = {1, 2, 3}

ikiKumeFarki = set1.difference(set2)    # set1'de olup set2'de olmayanlar
print(ikiKumeFarki)

ikiKumeFarki = set2.difference(set1)    # set2'de olup set1'de olmayanlar
print(ikiKumeFarki)

farkliliklar = set1.symmetric_difference(set2)  # ikisinde de ortak olmayanlar
print(farkliliklar)
# aynı işlem set1 - set2 veya set2 - set1 şeklinde de yapılabilir.

