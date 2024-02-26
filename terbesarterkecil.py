# input a, b dan c
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangankeempat:  "))
 # secara berurutan tulis kriteria untuk a, b, dan c
if a > b and a > c and a > d :
    print("Terbesar: ", a)
elif b > a and b > c and b > d:
    print("Terbesar: ", b)
elif c > a and c > b and c > d:
     print("Terbesar: ", c)
elif d > a and d > b and d > c:
     print("Terbesar: ", d)