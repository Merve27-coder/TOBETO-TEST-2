#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini 
#(VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input( "boyunuzu giriniz: "))
agirlik = float(input("kilonuzu giriniz: "))
Vki = agirlik/(boy*boy)
messageText1 = f"Vücut kitle indeksi: {Vki}"
print (messageText1)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("maaş giriniz: "))
zamOranı = float(input("zam oranını % olarak giriniz: "))
zamliMaas = float(maas+ (maas*zamOranı/100))
messageText2 =f"Yeni Maaşınız: {zamliMaas}"
print(messageText2)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.



#Kısa Yol
sayi1 = int(input("1.sayıyı giriniz: "))
sayi2 = int(input("2.sayıyı giriniz: "))
sayi3 = int(input("3.sayıyı giriniz: "))
messageText3= f"Max Sayı: {max(sayi1,sayi2,sayi3)}"
print(messageText3)




#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
import math
yaricap = int(input( "yarıçap giriniz: "))
pi = math.pi

daireAlan = pi*(yaricap*yaricap)
cevre = 2*pi*yaricap

print ("{message} {sonuc}".format(message="Dairenin Alanı: ", sonuc=daireAlan) )
print ("{message} {sonuc}".format(message="Dairenin Çevresi: ", sonuc=cevre) )

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız. 101 1001 11 

sayi= input("Bir sayı giriniz: ")
sayiTersi = sayi[::-1]
message1= " Girdiginiz sayi palindromdur." 
message2= " Girdiginiz sayi palindrom degildir." 
if sayi== sayiTersi :
  print("{message}".format(message= message1))
else:
   (print("{message}".format(message= message2)))