def kullanici_bilgisi():
    # Kullanıcıdan ad, yaş ve doğum yılı al
    ad = input("Adınızı girin: ")
    yas = int(input("Yaşınızı girin: "))
    dogum_yili = int(input("Doğum yılınızı girin: "))
    
    # Kullanıcı bilgilerini ekrana yazdır
    print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

def hesap_makinesi():
    # Kullanıcıdan iki sayı al
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    # Sayıların toplamını, farkını, çarpımını ve bölümünü hesapla ve yazdır
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Bölme hatası (sıfıra bölme)"

    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Çarpım: {carpim}")
    print(f"Bölüm: {bolum}")

# Ana program
kullanici_bilgisi()
hesap_makinesi()