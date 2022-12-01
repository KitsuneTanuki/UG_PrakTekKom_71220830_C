print("Periksa Kelipatan 9")
angka = int(input("Masukkan kelipatan 9 yang ingin diperiksa : "))

def kelipatan_sembilan(angka):
    bukti = angka%9
    return bukti

if kelipatan_sembilan(angka)==0:
    print("Benar")
else:
    print("Salah")
    print(angka%9)
    
    
