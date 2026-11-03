# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:08:33 2026

@author: senan
"""

sayi1 = int(input("sayi giriniz : "))
sayi2 = int(input("sayi giriniz : "))
islem = input("islem giriniz ( +, -, *, /, **, //: )")

#Toplama
if islem == "+" :
    sonuc = sayi1 + sayi2
    print("Toplam :" , sonuc)

#cikarma
elif islem == "-" :
    sonuc = sayi1 - sayi2
    print("Cikarma :" , sonuc)

#carpma
elif islem == "*" :
    sonuc = sayi1 * sayi2
    print("carpma :" , sonuc )

#bolme
elif islem == "/" : 
    if sayi2 == 0:
        print("hata : bir sayı sıfıra bölünemez")
    else:
        sonuc = sayi1 / sayi2
        print("bolme :" , sonuc)
#ussalma
elif islem == "**" :
        sonuc = sayi1 ** sayi2
        print("ussalma :" , sonuc)

#tambolme
elif islem == "//" :
    if sayi2 == 0:
        print("geçersiz işlem")
    else:
        sonuc = sayi1 // sayi2
        print("tambolme:" ,  sonuc)