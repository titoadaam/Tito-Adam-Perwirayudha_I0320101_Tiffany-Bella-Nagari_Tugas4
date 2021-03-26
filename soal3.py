beratkg = float(input("Masukan Berat Bagasi(KG): "))
beratlbs = beratkg * 2.2 <= 50
if beratlbs == True:
    print(f"{beratlbs}, Berat Dibawah Maksimal(50KG) Silahkan Masuk..")
else:
    print(f"{beratlbs}, Berat Melebihi Batas Maksimum(50KG). Kurangi Berat Bagasi Anda Sebelum Melanjutkan..")