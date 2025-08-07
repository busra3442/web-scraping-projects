import requests
from bs4 import BeautifulSoup


url = "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0"
}

html = requests.get(url,headers=headers).content

soup = BeautifulSoup(html,"html.parser")

liste = soup.find("div", class_="product-grid").find_all("div", class_="product-cr", limit=20)
for item in liste:
    kitapAdiDiv = item.find("div", class_="name ellipsis")
    kitapAdi = kitapAdiDiv.find("span").text.strip()

    kitapYazariDiv = item.find("div", class_="author compact ellipsis")
    kitapYazari = kitapYazariDiv.find("a").text.strip()

    kitapFiyatiDiv = item.find("div", class_="price")
    kitapFiyati = kitapFiyatiDiv.text.strip()

    print("*kitap adı:    " , kitapAdi , "\n*kitap yazarı: " , kitapYazari , "\n*kitap fiyatı: " , str(kitapFiyati) , "\n*******" )

# elde ettiğim verileri bir dosyaya kaydedebilirim örnek olması amacı ile aşağıya kod bloğumu ekledim

with open("top-20-books.txt","w", encoding="utf-8") as file:
    for item in liste:
        kitapAdiDiv = item.find("div", class_="name ellipsis")
        kitapAdi = kitapAdiDiv.find("span").text.strip()

        kitapYazariDiv = item.find("div", class_="author compact ellipsis")
        kitapYazari = kitapYazariDiv.find("a").text.strip()

        kitapFiyatiDiv = item.find("div", class_="price")
        kitapFiyati = kitapFiyatiDiv.text.strip()

        file.write(f"   Kitap Adı : {kitapAdi}\n")
        file.write(f"   Yazar     : {kitapYazari}\n")
        file.write(f"   Fiyat     : {kitapFiyati}\n")
        file.write("\n")





