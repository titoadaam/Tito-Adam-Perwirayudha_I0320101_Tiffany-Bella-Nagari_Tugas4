#Keluaran program biner
print("        KELUARAN DARI OPERATOR BITWISE")
print("""
==================================================""")

a = 4       #4 = 0000 0100
b = 11      #11 = 0000 1011

#4 | 11
c = a | b       #15 = 0000 1111
print("Hasil dari 4|11 adalah :", c)

#4 >> 11
c = a >> b      #0 = 0000 0000
print("Hasil dari 4>>11 adalah :", c)

#4 ^ 11
c = a ^ b       #15 = 0000 1111
print("Hasil dari 4 ^ 11 adalah :", c)

#~4
c = ~a          #-5 = 0000 0101
print("Hasil dari ~4 adalah :", c)

#11 & 4
c = b & a       #0 = 0000 0000
print("Hasil dari 11&4 adalah :", c)

print("""   TERIMA KASIH TELAH MAMPIR
>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<""")