import requests
from bs4 import BeautifulSoup
import numpy as np

# IMDb Top 10 sayfası
url = "https://www.imdb.com/chart/top/?ref_=hm_nv_menu"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li", limit=10)

film_listesi = []
puanlar = []

# Verileri listelere ekle
for item in liste:
    filmAdi = item.find("h3", {"class": "ipc-title__text"}).text
    puan_text = item.find("span", {"class": "ipc-rating-star"}).text
    puan = float(puan_text.split()[0])  # Örn: "9.2" -> 9.2
    film_listesi.append(filmAdi)
    puanlar.append(puan)

# Numpy ile istatistikler
puanlar_np = np.array(puanlar)

en_yuksek = np.max(puanlar_np)
en_dusuk = np.min(puanlar_np)
ortalama = np.mean(puanlar_np)
std_sapma = np.std(puanlar_np)

print("🎬 IMDb Top 10 Film Puanları")
for film, puan in zip(film_listesi, puanlar):
    print(f"{film}: {puan}")

print("\n📊 Numpy ile İstatistikler:")
print("En yüksek puan:", en_yuksek)
print("En düşük puan:", en_dusuk)
print("Ortalama puan:", round(ortalama, 2))
print("Standart sapma:", round(std_sapma, 2))

# Sonuçları dosyaya kaydet
with open("imdb_top10_numpy.txt", "w", encoding="utf-8") as file:
    file.write("🎬 IMDb Top 10 Film Puanları\n")
    for film, puan in zip(film_listesi, puanlar):
        file.write(f"{film} - {puan}\n")

    file.write("\n📊 İstatistikler:\n")
    file.write(f"En yüksek puan: {en_yuksek}\n")
    file.write(f"En düşük puan: {en_dusuk}\n")
    file.write(f"Ortalama puan: {round(ortalama, 2)}\n")
    file.write(f"Standart sapma: {round(std_sapma, 2)}\n")

print("\n✅ 'imdb_top10_numpy.txt' dosyası oluşturuldu.")
