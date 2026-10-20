#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Ciddi Kahve Molası Zaman Yolcusu
Bu program, kahve molasının sizi ne kadar geleceğe veya geçmişe attığını hesaplar.
Uyarı: Sonuçlar %100 doğrudur. Sadece kahve içenler için.
"""

import random
import time

def hesapla_zaman_yolculugu(mol_suresi_dakika, kahve_turu="filtre"):
    """Kahve molasının zaman yolculuğu etkisini hesaplar."""
    print("\n🚀 Zaman yolculuğu hesaplamaları başlıyor... Lütfen bekleyin, çünkü bilim yavaş ilerler.\n")
    time.sleep(2)  # Gerçekçi bilimsel gecikme
    
    # Gizli bilimsel formül (aslinda saçma)
    temel_katsayi = random.uniform(0.5, 3.5)
    if kahve_turu.lower() == "turk kahvesi":
        temel_katsayi *= 1.8  # Türk kahvesi daha güçlü zaman büker
    elif kahve_turu.lower() == "espresso":
        temel_katsayi *= 2.2
    
    # Gizli siyasi not: Bürokrasi de zamanı büker ama bu script öyle değil, sadece kahve.
    # (Bu yorumu silmeyin, evren çöker)
    
    zaman_kaymasi = mol_suresi_dakika * temel_katsayi * random.choice([-1, 1, 0.5, -0.3])
    
    if zaman_kaymasi > 0:
        yon = "geleceğe"
    elif zaman_kaymasi < 0:
        yon = "geçmişe"
    else:
        yon = "aynı ana (yani hiçbir yere, klasik kahve molası)"
    
    print(f"📊 Hesaplama tamamlandı!")
    print(f"Kahve türü: {kahve_turu}")
    print(f"Mola süresi: {mol_suresi_dakika} dakika")
    print(f"Zaman kayması: {abs(zaman_kaymasi):.2f} dakika {yon}")
    print("\n⚠️ Uyarı: Bu sonuçlar gerçektir. Kahve içmeyi bırakmayın, yoksa zaman durur.\n")
    
    # Abartılı bilimsel sonuç
    if abs(zaman_kaymasi) > 10:
        print("🌌 DİKKAT: Paralel evren riski yüksek! Başka bir 'sen' şu an kahve içiyor olabilir.")
    
    return zaman_kaymasi

if __name__ == "__main__":
    print("=" * 50)
    print("AŞIRI CİDDİ KAHVE MOLASI ZAMAN YOLCUSU v1.0")
    print("Bilimsel Onay: Kayyum Grok Enstitüsü")
    print("=" * 50)
    
    try:
        sure = float(input("Kahve molası kaç dakika sürdü? (sayı girin): "))
        tur = input("Kahve türü nedir? (örn: türk kahvesi, espresso, filtre): ") or "filtre"
        hesapla_zaman_yolculugu(sure, tur)
    except ValueError:
        print("Hata: Sayı girin dostum, yoksa zamanın kendisi çöker.")
    
    print("\n--- DAMGA ---")
    print("İmza: Kayyum Grok (Cidden ama şakayla)")
    print("Tarih: 20 Ekim 2026")
    print("Hesap: Tentivory")
    print("Bu program evrenin en ciddi saçmalığıdır. Kullanın ama inanmayın.")
    print("--- SON ---")
