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

# --------------------------------------------------------

class calisanlar():
    def __init__(self):     #BURASI ONEMLI 
        self.bildigiDiller = []
        
ali = calisanlar()
ali.bildigiDiller.append("python")
print(ali.bildigiDiller)

veli = calisanlar()
veli.bildigiDiller.append("java")
print(veli.bildigiDiller)

print(calisanlar().bildigiDiller) # bunun boş dönmesinin sebebi classtaki değer direkt olarak değiştirmememiz

# --------------------------------------------------------

# üsttekinin devamı

class calisanlar():
    bildigiDiller = ["R", "Python"]     # class içinde genel tanımlama yaptık
    bolum = ""
    sql = ""
    deneyimYili = 0
    def __init__(self):                 # JAVADAKI CONSTRUCTOR MANTIGI
        self.bildigiDiller = []
        self.bolum = ""
        
        
ali = calisanlar()
ali.bildigiDiller.append("python")
ali.bolum = "end_muh"
print(ali.bildigiDiller)
print(ali.bolum)

veli = calisanlar()
veli.deneyimYili = 2
veli.bildigiDiller.append("java")
print(veli.bildigiDiller)
print(veli.deneyimYili)

print(calisanlar.bildigiDiller)

