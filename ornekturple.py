birimler = ("bit", "inç", "byte", "hertz", "piksel","hertz")
degerler = (2,5,3.14)
print(birimler)
#print(type(birimler))
#print(birimler[3]) #Tuple elemanlarına ulaşma: Listelerdeki gibi indeks kullanılır.
#print(birimler[-1]) #Listelerde olduğu gibi negatif indekslerde kullanılabilir
#print(birimler[1:3]) #Listelerde olduğu gibi başlangıç ve bitiş indeksleri verilerek istenilen aralık yazdırılabilir.
"""Tuple elemanlarını değiştirme: Tuple veri tipi tanımlanırken elemanların değiştirilemeyeceğinden bahsedildi.
Eğer tuple veri tipi listeye çevrilirse elemanlar değiştirilebilir."""
"""yeni_birimler=list(birimler)
yeni_birimler[0]="BİT"
print(yeni_birimler)"""

"""Elemanın olup olmadığını sorgulama: Tuple veri tipinde de listelerde olduğu gibi in operatörü ile bir
elemanın listede olup olmadığı kontrol edilebilir. Eleman tuple’daysa True; yoksa False değerleri üretilir."""
#print("inç" in birimler)
#print(birimler.index("inç"))
#print(len(birimler)) #Tuple uzunluğunu bulma: len fonksiyonu ile tuple’ın eleman sayısı bulunur.
#Tuple içinde bir elemanın sayısını bulma: Bu işlem için listelerde olduğu gibi count fonksiyonu kullanılır.
#print(birimler.count("hertz"))
#degerler=degerler+birimler
print(degerler)

