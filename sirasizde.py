"""Aşağıdaki sözlükleri oluşturarak sizlerden istenen işlemleri yapınız.
sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
a) sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız.
b) sozluk isimli sözlüğün değerlerini ekrana yazdırınız.
c) sozluk isimli sözlüğü içi boş bir sözlük hâline getiriniz.
ç) sozluk isimli sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz.
d) sozluk isimli sözlüğün içinde sanatçı anahtarının olup olmadığını sorgulayınız.
e) sozluk isimli sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olarak değiştiriniz.
f) sozluk isimli sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırınız."""

sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
#print(sozluk)
meslekler=sozluk.copy()
#meslekler.clear()
#meslekler["Matematikçi"]="Cahit Arf"
#print("sanatçı" in meslekler)
#meslekler['Bilim insanı']='Canan Dağdeviren'
print(meslekler["Şair"])