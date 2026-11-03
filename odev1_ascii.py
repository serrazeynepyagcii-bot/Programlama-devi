# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:05:22 2026

@author: senan
"""

print(f"{'ASCII KODU':<10} | {'KARAKTER'}")
print(f"{'-'*10}-|{'-'*18}")

for i in range(128):

    if i <= 31 or i == 127:
        karakter = "Kontrol karakteri"
        
    elif i == 32:
        karakter = "[boşluk]"
        
    else:
        karakter = chr(i)
    print(f"{i:<10} | {karakter}")