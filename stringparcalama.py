veri = "Bilişim Teknolojileri Kadirli"
metin="ilkbahar,yaz,sonbahar,kış"
# veri_bolum = veri.split(" ") #veri değişkenini boşluktan itibaren bölüyoruz.
metin_bolum = metin.split(",") #metin değişkenini virgüllerden bölüyoruz.
metin_bolum_ikieleman = metin.split(",",2) #1 parametresi vererek metni sadece 2 parçaya bölüyoruz.
# print(veri_bolum)
# print(len(veri_bolum))
print(metin_bolum)
print(metin_bolum_ikieleman)