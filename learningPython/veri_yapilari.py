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

sozluk["GBM"] = "Gradient Boosting Mac"
print(sozluk)

