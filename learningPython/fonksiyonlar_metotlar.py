def isimleriListele():
    isimler = ["ahmet", "burak", "mehmet", "ugur", "a", "b", "z"]
    for i in range(len(isimler)):
        print(isimler[i])
        
isimleriListele()

# --------------------------------------------------------

def kareAl(x):
    print("girilen " + str(x) +  " sayisinin karesi: " + str(x**2))
    
kareAl(5)
