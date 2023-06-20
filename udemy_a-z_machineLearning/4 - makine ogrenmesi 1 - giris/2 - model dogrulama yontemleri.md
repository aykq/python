# **Model Doğrulama Yöntemleri**

+ Modellerin ürettiği sonuçların doğru değerlendirilmesi çalışmalarıdır.

## =======================================

## **1. Holdout Yöntemi**

![Alt text](<photos/8 - holdout yontemi.png>)

+ Türkçe olarak sınama seti yaklaşımı.
+ Eğitim setiyle kurulan modelin performansı test seti ile ölçülür.
+  Gözlem sayısı az ise eğitim ve test setini bölme konusunda sıkıntılar yaşanabilir.

## =======================================

## **2. K-Katlı Çapraz Doğrulama (k fold cross validation)**

![Alt text](<photos/9 - k-katli capraz dogrulama.png>)

 + Eğitim seti 5 farklı parçaya ayrılır. Ayrılan 5 parçadan 1 tanesi dışarıda bırakılarak kalan 4 parça ile model oluşturulur.
 + Dışarıda kalan parça test seti olarak kullanılır. Oluşturulan modelin başarısı bu parça ile test edilir.
 + Her iterasyonda bir diğer parça dışarıda bırakılarak aynı işlemler tekrar edilir.
 + Kendi içerisinde train-test yaklaşımı vardır.
 + Eğitim hatası = validation, validasyon hatası.
 + Bu 5 parçayla olan eğitim sonucunda eğitim hataları olabilir. Eğitim hatası, test hatasının kötü bir tahmincisidir.

 ## =======================================

## **3. Leave One Out Yöntemi**

![Alt text](<photos/10 - leave one out yontemi.png>)

+ K-Katlı çapraz doğrulama yönteminin özel bir halidir.
+ n tane gözlem varsa n tane küme vardır.
+ Model n-1 adet örnek ile eğitilir ve dışarıda kalan 1 tane örnek ile test edilir.

## =======================================

## **4. Bootstrap Yöntemi**

![Alt text](<photos/11 - bootstrap yontemi.png>)

+ Orijinal veri seti içerisinden yerine koymalı örnekleme (bootstrap) yöntemiyle örnekler çekilir.
+ Elde edilen örneklemlerin her birisinin hata değerinin ortalaması alınarak test hatası belirlenir.