try:
    suhu = input("masukkan suhu tubuh anda : ")
    if int (suhu) >= 38:
        print(" KAMU DEMAM")
    else :
        print("KAMU TIDAK DEMAM")
except :
    print("masukkan input yang benar")
    