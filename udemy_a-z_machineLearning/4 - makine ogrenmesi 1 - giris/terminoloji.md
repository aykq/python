# **Kavramlar**

## 1. **Bağımlı değişken & bağımsız degişken**

![Alt text](<photos/1 - bagimli - bagimsiz degisken.png>)

+ x1, x2, x3 ve x4 bağımsız değişkenler 
+ y ise bağımlı değişken

## =======================================


## 2. **Gözetimli, gözetimsiz, yarı gözetimli öğrenme**

![Alt text](<photos/2 - gozetimli gozetimsiz ogrenme.png>)

+ veri setimizin içinde yanıt değişkeni var ise (y değişkeni) (soldaki tablo) bu gözetimli öğrenmedir.

+ gözetimsiz öğrenme ise içinde y değişkeninin yani bağımlı değişkenin olmadığı öğrenmedir.

## =======================================

## **3. Regresyon ve Sınıflandırma**

![Alt text](<photos/3 - regresyon ve siniflandirma.png>)

+ regresyonda bağımlı değişken süreklidir. (soldaki tablo)
+ sınıflandırmada ise 1 - 0, erkek - kadın şeklindedir.

## =======================================

## **4. Değişken Türleri**

+ ## Değişken Türleri
    + Sayısal Değişkenler (nicel, kantitatif)
    +Kategorik Değişkenler (nitel, kalitatif)

+ ## Ölçek Türleri
    + Sayısal değişkenler için: aralık ve oran
    + Kategorik değişkenler için: nominal ve ordinal

## =======================================

## **5. Test - Train Ayrımı**

![Alt text](<photos/4 - test train ayrimi.png>)

+ Elimizdeki veri setini 2'ye ayırıp bir kısmıyla eğitip bir kısmıyla eğittiğimiz modelin performansını test edelim fikrine dayanır.

## =======================================

## **6. Değişken Mühendisliği**

+ Kişinin kendisinin veya otomatikleştirdiği sistemin, veri setinin oluşması aşamasında veri tabanı içerisinden değişkenler oluşturma işlemidir.

## =======================================

## **7. Değişken Seçimi**

![Alt text](<photos/5 - degisken secimi.png>)

+ Renklerini kaybetmiş olan değişkenler, y bağımlı değişkenini tahmin etme söz konusu olduğunda başarılı olmayan, ayırt ediciliği olmayan ve bir şekilde kullanıcı tarafından veya otomatik olarak çalışmanın dışarısında bırakılmış değişkenlerdir. renkli olanlar ise seçilmiş değişkenlerdir.

## =======================================

## **8. Model Seçimi**

## Model için 2 durum söz konusu:

+ Birincisi: Oluşabilecek değişken kombinasyonları ile oluşturulan modeller arasından en iyi modelin seçilmesi

+ İkincisi: Kurulan birbirinden farklı modeller arasından model seçimi

## Model neye göre seçilir?

+Regresyon için açıklanabilirlik oranı ve RMSE benzeri bir değer.

+ Sınıflandırma için doğru sınıflandırma oranı benzer bir değer.

## =======================================

## **9. Aşırı Öğrenme**

+ Eğittiğimiz model kendi içerisinde çok iyi olsa da, verdiğimiz veri setini çok iyi öğrenmiş olsa da hiç görmediği veri seti veya gerçek hayat verisine uyarladığımızda model patlamış oluyor. Hata başarısı düşmüş oluyor.

## =======================================

## **10. Deterministik Modeller ve Stokastik Modeller**

![Alt text](<photos/6 - deterministik - stokastik model.png>)

+ Değişkenler arasında kesin bir ilişki olduğunu varsayan modellere deterministik modeller denir (soldaki). 
+ Grafikte x'e vereceğimiz herhangi bir değere karşılık, y'nin alacağı değeri kesin olarak biliriz.
---
+ Tesadüfi hata barındıran, x'e karşılık y'nin alacağı değerleri ortaya çıkaran, rastsallık kavramının olduğu, hata barındırma durumunun da olduğu olasılıksal modellerdir (sağdaki).

## =======================================

## **11. Doğrusal ve Doğrusal Olmayan Modeller**

![Alt text](<photos/7 - dogrusal - dogrusal olmayan modeller.png>)