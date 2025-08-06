import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=hm_nv_menu"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("ul",{"class":"ipc-metadata-list"} ).find_all("li",limit=10)
# ul elemanlarını getir bunlar içerisinden class ismi bu olan elemanı getir ve find_all ile bu elemntin altındaki
# bütün li leri getirir böylece döngü ile ulaşabileceğimiz bir liste elde etmiş oluruz

for item in liste:
    filmAdi = item.find("h3",{"class":"ipc-title__text"}).text
    puan = item.find("span", {"class": "ipc-rating-star" }).text
    print(filmAdi, puan)


# burdan elde ettiğim bilgileri ister bir dosyaya kaydederim ister exel tablosu hazırlarım örneğin bir dosyaya
# kaydedeceksem şu kod bloğunu kullanabilirim

with open("imdb_top10.txt", "w", encoding="utf-8") as file:
    for item in liste:
        filmAdi = item.find("h3", {"class": "ipc-title__text"}).text
        puan = item.find("span", {"class": "ipc-rating-star"}).text
        file.write(f"{filmAdi} - {puan}\n")
