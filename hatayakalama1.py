print("Program başladı")
try:
    sayi = int(input("Bir sayı yazınız: "))
    karesi = sayi * sayi
    print("Sayının karesi:", karesi)
except ValueError:
    print("Sayı girmediniz!")
print("Program sona erdi!")