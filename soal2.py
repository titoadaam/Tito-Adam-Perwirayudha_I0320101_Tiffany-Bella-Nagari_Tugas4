x1 = input("Masukan Angka Pertama : ")
x2 = input("Masukan Angka Kedua : ")
x=x1+" "+x2
soal=x.split(" ")
if int(soal[0]) >= int(soal[1]):
    print("angka kedua ({x2}) dapat dikali dengan {int(soal[0]) // int(soal[1])} untuk mendekati angka pertama ({x1}) ")
elif int(soal[0]) <= int(soal[1]):
    print("angka pertama ({x1}) dapat dikali dengan {int(soal[1]) // int(soal[0])} untuk mendekati angka kedua ({x2}) ")
else:
    print("TIDAK TERDEFINISI")
