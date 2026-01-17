print("==ALAT PENGUKUR BADAN IDEAL==")

lanjut = "y"

while lanjut == "y":
    try:
        Tinggi = float(input("Masukkan Tinggi Badan : "))
        Berat = float(input("Masukkan Berat Badan : "))

        if Tinggi <= 0 or Berat <= 0:
            print("Error: Tinggi dan Berat harus lebih dari 0!")
            continue

        Berat_ideal = abs(Tinggi - 110)
        print(f"Target Berat Ideal Anda: {Berat_ideal} kg")

        if Berat >= Berat_ideal + 10:
            print("Hasil: Berat Anda Melebihi Batas Ideal")
        elif Berat <= Berat_ideal - 10:
            print("Hasil: Berat Anda Kurang Ideal")
        else:
            print("Hasil: Berat Anda Sudah Ideal")

        lanjut = input("Apakah Anda Ingin Melanjutkan? (y/n) : ")

        if lanjut == "n":
            print("Terimakasih Telah Menggunakan Project Pengukur Badan Ideal ^^")
            break

    except ValueError:
        print("Error: Masukkan angka yang valid (gunakan titik untuk desimal)!")