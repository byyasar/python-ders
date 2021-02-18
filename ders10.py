"""Kullanıcının girdiği kısa ve uzun kenar değerlerine göre dikdörtgenin alanını ve çevresini hesaplayınız.
Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz. Burada noktalar kullanıcının
gireceği değerlere göre değişecektir."""

kisa=int(input("kısa kenarı giriniz: "))
uzun=int(input("uzun kenarı giriniz: "))
alan=kisa*uzun
cevre=(kisa+uzun)*2
print("Dikdörtgenin Alanı:",alan,"Çevresi:",cevre)