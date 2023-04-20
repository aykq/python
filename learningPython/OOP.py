# NESNE YONELIMLI PROGRAMLAMA

# 1 - class

class test():
    print("bu bir sinif örnegidir")
    
# --------------------------------------------------------

# class özellikleri

class calisanlar():
    bolum = ''
    sql = "evet"
    deneyim = 0
    bildigiDiller = []
    
# sınıfların özelliklerine erişmek
print(calisanlar.bolum)
print(calisanlar.sql)

# sınıfların özelliklerini değiştirmek
calisanlar.sql = "hayir"
print(calisanlar.sql)

# sınıf örneklendirmesi - o class'a ait nesneler oluşturma - class'ın özelliklerini taşır
ali = calisanlar()
print(ali.sql)
print(ali.deneyim)
ali.bildigiDiller.append("python")  # bu şekilde değiştirme yaptığımızda classta tanımlanan değer de değişir
print(ali.bildigiDiller)

veli = calisanlar()
print(veli.sql)
print(veli.bildigiDiller)   # classta tanımlanan değer değiştiği için "python" olarak çıktı verir

# aşağıda bunun çözümünün nasıl yapıldığı var