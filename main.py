# from math import pi
# #soal no 1
# #celengan andi yang berbentuk balok
# panjang= 20 #cm
# lebar= 13 #cm
# tinggi= 7 #cm
# hasil1= panjang * lebar * tinggi

# #celengan andi yang berbentuk tabung
# diameter= 14 #cm
# jari_jari= diameter / 2
# luas_selimut= 440 #cm^2
# tinggi_tabung= luas_selimut / (2 * pi * jari_jari )
# volume_tabung= pi * (jari_jari ** 2) * tinggi_tabung
# print("membantu andi menghitung volume dari celengan nya yang berbentuk balok")
# print("jika diketahui celengan andi yang berbentuk balok  adalah:")
# print("panjang nya", panjang, "cm")
# print("lebar nya", lebar, "cm")
# print("dan tinggi nya", tinggi, "cm")
# print("mari kita tentukan volume celengan balok milik andi")
# panjang_balok =int(input(f"jika panjang balok tersebut:"))
# lebar_balok =int(input(f"jika lebar balok tersebut :"))
# tinggi_balok =int(input(f"dan tinggi balok tersebut:"))
# volume_balok = panjang_balok * lebar_balok * tinggi_balok
# print("maka volume celengan andi yang berbentuk balok adalah:",volume_balok,"cm^3")
# #menghitung volume celengan yang berbentuk tabunng
# print("sedangkan diketahui celengan andi yang berbentuk tabung adalah:")
# print("diameter nya ",diameter, "cm", "artinya jari-jari dari diameter balok adalah jari-jari dibagi 2 =", jari_jari )
# print("sedangkan luas selimut nya adalah", luas_selimut, "cm^2", "sebelum menghitung volume tabung" )
# print("mari tentukan tinggi dari celengan andi yang berbentuk tabung")
# luas_selimut2 =int(input(f"jika diketahui luas selimut dari celengan tabung adalah:"))
# jari_jari2 =float(input(f"dan jari-jari dari celengan tersebut adalah:"))
# tinggi_tabung2 = luas_selimut2 / (2 * pi * jari_jari2 )
# print("dengan memakai rumus: luas_selimut / (2 * pi * jari_jari ) maka tinggi tabung adalah ", tinggi_tabung2, "cm")
# print("jika kita sudah menentukan tinggi nya mari kita tentukan volume celengan tabung milik andi")
# print("yakni dengan memakai rumus: pi * (jari_jari ** 2) * tinggi_tabung ")
# print("maka bisa ditentukan volume celengan andi yang berbentuk tabung memiliki volume:",volume_tabung,"cm^3")

#soal no2 membantu darmaji menghitung deret aritmatika
# RUMUS
# Mencari d/selisih
# 2(11 - 4.d) + 18.d = 52
# 22 - 8.d + 18.d = 52
# 10.d = 30
# d = 3

# Mencari a/suku pertama
# a = suku_ke_5 - 4 * d 
# a = hasil suku yang sudah di ketahui - (suku ke berapa-1)* selisih
# a = 11 - 4 *3
# a = -1 

# Diketahui:
# a = suku pertama = -1
# d = Selisih setiap suku = 3

# Suku ke-5 (a + 4.d) = 11

# Suku ke-8 (a + 7.d) + Suku ke-12 (a + 11.d) = 52

# DIKETAHUI
suku_ke_5 = 11
suku_ke_8_dan_12 = 52
d = 3
a = suku_ke_5 - 4 * d

suku=int(input("Masukkan suku yang ingin anda cari: "))

Mencari_suku =a+(suku-1)*d

print(f"Suku ke {suku} bernilai = {Mencari_suku}"  )

# Jumlah dari 8 suku pertama: S8 = (n/2)(2a + (n-1)d)
n =int(input("Masukkan suku deret aritmatika yang ingin di cari : "))
jumlah_8_suku =int(n / 2) * (2 * a + (n - 1) * d)

print(f"Jumlah 8 suku pertama dari deret aritmatika adalah: {jumlah_8_suku}")


# # #soal no3
# usd = 35
# perkiraan_kurs_sesuai_tanggal_pratikum = 15000
# print("kali ini kita akan membantu suraji untuk menukarkan dollar pada rupiah")
# uang_dollar = int(input(f"jika suraji mempunyai uang dollar sebanyak:"))
# kurs = int(input(f"sedangkan kurs mata uang negara kita sekarang adalah:"))
# total_nominal = uang_dollar * kurs
# print("maka total nilai uang yang didapatkan suraji dari hasil penukaran nya adalah:",total_nominal, "IDR")

# #soal no4
# import math
# a = 7 #total orang
# b = 4 #orang yang dipilih

# print("kali ini kita akan membantu darsono untuk menyusun tim dari beberapa orang")
# print("darsono disini memiliki total 7 orang dan ingin memilih 4 orang untuk masuk timnya")
# print("disini darsono ingin tau berapa banyak cara untuk membentuk timnya, jadi mari kita bantu")

# cara_membentuk_tim = math.comb(a,b)
# print("jadi untuk menghitung beberapa cara membentuk tim:", cara_membentuk_tim, "cara")




