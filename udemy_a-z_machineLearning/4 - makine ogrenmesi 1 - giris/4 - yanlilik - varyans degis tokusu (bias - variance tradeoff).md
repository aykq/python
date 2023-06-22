# **Yanlılık - Varyans Değiş Tokuşu (Bias - Variance Tradeoff)**
Modellerin tahmin başarısının değerlendirilmesi 

 ## =======================================

![Alt text](<photos/14 - bias variance.png>)

Yanlılık: Gerçek değerler ile tahmin edilen değerler arasındaki mesafeyi ifade eder.

Varyans: Değişkenlik. Bir fonskiyonun esnekliği, hassaslığıdır.

+ Underfitting grafiğindeki düz çizgi gerçek değerleri, noktalar ise tahmin edilen değerleri temsil eder. 
+ Fonskiyonumuz gerçek değerleri tahmin etme konusunda yeteri kadar başarılı değil. Yani az öğrenmiş, eksik öğrenmiş.
+ Böyle grafiklere underfitting: az öğrenmiş yorumu yapılır. Sebebi ise yüksek yanlılık.

 ## =======================================

 + Varyansın yüksek olması, veri setinin içindeki değerleri esnek bir şekilde temsil etmek demek. Fonskiyonun esnek olması varyans durumunun yüksek olduğu anlamına gelir. 
 + Biz bu fonskiyonun yani varyansın bu kadar yüksek olmasını istemeyiz. Tahmin fonksiyonunun esnekliği arttıkça, veri setinin içerisindeki yapıyı temsil etme kabiliyeti arttıkça varyansı artar, yanlılığı azalır. Bu durum bir noktaya kadar o modeli başarılı kılacaktır ama bir noktadan sonra başarısızlığa iter. 
 + Varyansın yüksek olması, o modelin genel değil özel bir model olduğu anlamına gelir. Amacımız genellenebilir modeller ortaya çıkarmaktır. 
 + Bu model, veri setinin yapısını öğrenmek yerine direkt ezberledi, öğrenemedi. Bu durum overfitting.
 + Öğrenemediğinden dolayı hiç görmediği bazı gözlemler gösterildiğinde ezber yaptığından dolayı hatalar üretmiş olacak. Overfitting durumunu bu şekilde anlayabiliriz.

 ## =======================================

# **Eğitim Hatası vs Test Hatası**

![Alt text](<photos/14.1 - egitim hatasi vs test hatasi.png>)

+ Modelin karmaşıklığı: modelin esnekliği, varyansı olarak düşünebiliriz.
