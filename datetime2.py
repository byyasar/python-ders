import datetime
import locale
# locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')
locale.setlocale(locale.LC_ALL,"tr_TR")
an = datetime.datetime.now()
tarih_metni = '17 Mayıs 2021 saat 14:32:11'
# print("Metin halindeki tarih = ", tarih_metni)

tarih_nesnesi = datetime.datetime.strptime(tarih_metni,'%d %B %Y saat %H:%M:%S')
# print("Tarih nesnesi = ",tarih_nesnesi) 
# print(tarih_nesnesi.year)
# print(tarih_nesnesi.month)
print(tarih_nesnesi.strftime('%A'))





# print(an.strftime('%Y')) # Yıl
# print(an.strftime('%X')) # Saat
# print(an.strftime('%d')) # Gün - ayın kaçıncı günü
# print(an.strftime('%A')) # Gün - İsim olarak
# print(an.strftime('%B')) # Ay - İsim olarak
# print(an.strftime("%d-%m-%Y"))
# print(an.strftime("%d %B %Y %A"))
# print(an.strftime("%X"))
