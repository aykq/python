# try - except (javadaki try - catch)

# paydada 0 olamayacağı için hata alınır.

a = 10
b = 0
print(a/b)

a = 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("!!! paydada 0 olamaz !!!")

# ========================================================


a = 10      # type error alınır.
b = "2"
print(a/b)

a = 10
b = "1"
try:
    print(a/b)
except:
    print("!!! type error !!!")

# ========================================================


