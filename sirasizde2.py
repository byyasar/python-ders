
# a) önemli_bilgiler isimli sözlüğün değerlerini ekrana yazdırınız.
# b) önemli_bilgiler isimli sözlüğü siliniz.
# c) önemli_bilgiler isimli sözlükten Acil Çağrı Merkezi anahtarını ve değerini siliniz.
# ç) önemli_bilgiler isimli sözlükte Sağlık Bakanlığı İletişim Merkezi olup olmadığını sorgulayınız.
# d) önemli_bilgiler isimli sözlüğü içi boş bir sözlük hâline getiriniz.


onemli_telefonlar= {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
#print(onemli_telefonlar.values())
#del onemli_telefonlar
onemli_telefonlar.clear()
#onemli_telefonlar.pop("Acil Çağrı Merkezi")
#print("Milli Eğitim Bakanlığı İletişim Merkezi" in onemli_telefonlar)
print(onemli_telefonlar)
