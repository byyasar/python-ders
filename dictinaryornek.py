sozluk1 = {"Mesleğiniz":"Öğrenci", "Alanınız":"Bilişim", "Yaşadığınız Yer":"Ankara" }
sozluk2 = {"Mesleğiniz":"Öğretmen", "Alanınız":"Bilişim", "Yaşadığınız Yer":"Osmaniye" }
#print(sozluk1["Alanınız"]=="Bilişim")
yeni_sozluk={"SOZLUK2":sozluk2,"SOZLUK1":sozluk1}
print(yeni_sozluk)

#print(sozluk.keys())
#print(sozluk.values())
#sozluk["Doğum Tarihi"]="1980"
#print(sozluk)
#sozluk["Doğum Tarihi"]="2010"

#print("Alanınız" in sozluk) #Sözlükte Alanınız anahtarının olup olmadığı kontrol edilmiştir.
#print(len(sozluk)) #Burada eleman sayısının anahtar-değer ikilileri olarak hesaplanacağını unutmayınız.
#print(sozluk)
#sozluk.pop("Mesleğiniz")
#del sozluk #del fonksiyonu ile sözlük tamamen silinebilir
#sozluk.clear() #Sözlüğü silmek yerine içini boşaltmak için clear() fonksiyonu kullanılır.
#yeni_sozluk=sozluk.copy()
#print(yeni_sozluk)
