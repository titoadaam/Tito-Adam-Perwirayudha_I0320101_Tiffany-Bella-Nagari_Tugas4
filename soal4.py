print("""
SELAMAT DATANG
Silahkan isi form berikut untuk melanjutkan
""")
#pesaratan
usia = 21
kualifikasi = "Y"
usia = int(input("Masukan Usia Mu: "))
kualifikasi = input("Apakah anda sudah melalui kualifikasi? (Y/N): ")
if usia >= 21 and kualifikasi.upper() == "Y" :
    print("Anda dapat mendaftar kursus")
else :
    print("Anda tidak dapat daftar di kursus")