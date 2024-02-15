1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

def vucut_kitle_indeksi(boy, kilo):
    vki = kilo / (boy ** 2)
    return vki

boy = float(input("Boyunuzu (metre cinsinde) giriniz: "))
kilo = float(input("Kilonuzu (kilogram cinsinde) giriniz: "))

vki = vucut_kitle_indeksi(boy, kilo)
print("Vücut Kitle İndeksi (VKİ): {:.2f}".format(vki))

2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

def zamli_maas(haftalik_maas, zam_orani):
    zam_miktari = haftalik_maas * (zam_orani / 100)
    zamli_maas = haftalik_maas + zam_miktari
    return zamli_maas

haftalik_maas = float(input("Haftalık maaşı giriniz: "))
zam_orani = float(input("Zam oranını giriniz (% olarak): "))

zamli_maas = zamli_maas(haftalik_maas, zam_orani)
print("Zamlı maaş: {:.2f}".format(zamli_maas))

3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

def en_buyuk_bul(sayi1, sayi2, sayi3):
    en_buyuk = sayi1
    if sayi2 > en_buyuk:
        en_buyuk = sayi2
    if sayi3 > en_buyuk:
        en_buyuk = sayi3
    return en_buyuk

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))

en_buyuk = en_buyuk_bul(sayi1, sayi2, sayi3)
print("En büyük sayı: ", en_buyuk)

4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

import math

def daire_alani_cevresi(yaricap):
    alan = math.pi * yaricap ** 2
    cevre = 2 * math.pi * yaricap
    return alan, cevre

yaricap = float(input("Dairenin yarıçapını giriniz: "))

alan, cevre = daire_alani_cevresi(yaricap)
print("Dairenin alanı:", alan)
print("Dairenin çevresi:", cevre)

5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

def palindrom_mu(sayi):
    sayi_str = str(sayi)
    tersi_str = sayi_str[::-1]
    if sayi_str == tersi_str:
        return True
    else:
        return False

sayi = input("Bir sayı giriniz: ")

if palindrom_mu(sayi):
    print("Girdiğiniz sayı bir palindromdur.")
else:
    print("Girdiğiniz sayı bir palindrom değildir.")


    

