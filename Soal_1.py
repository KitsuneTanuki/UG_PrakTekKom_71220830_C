print("=========================")
print("Operasi Matematika")
print("1. Jumlah   [+]")
print("2. Kurang   [-]")
print("3. Kali     [*]")
print("4. Bagi     [/]")
print("=========================")
operasi = input("Pilih Operasi (1/2/3/4): ")
print("=========================")

def penjumlahan(B1,B2):
    plus = B1+B2
    return plus

def pengurangan(B1,B2):
    minus = B1-B2
    return minus

def perkalian(B1,B2):
    multiple = B1*B2
    return multiple

def pembagian(B1,B2):
    devide = B1/B2
    return devide

B1 = int(input("Masukkan bilangan pertama : "))
B2 = int(input("Masukkan bilangan kedua : "))
if operasi == "1":
    print("Hasil Operasi dari",B1,"+",B2," =",penjumlahan(B1,B2))
elif operasi == "2":
    print("Hasil Operasi dari",B1,"-",B2," =",pengurangan(B1,B2))
elif operasi == "3":
    print("Hasil Operasi dari",B1,"*",B2," =",perkalian(B1,B2))
else:
    print("Hasil Operasi dari",B1,"/",B2," =",pembagian(B1,B2))
    

