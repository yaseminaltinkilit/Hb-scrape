import requests
from bs4 import BeautifulSoup
import lxml
import xlsxwriter


workbook = xlsxwriter.Workbook('veriler.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,"Ürün İsimleri")
worksheet.write(0,1,"Ürün Fiyatları")
satirSayisi=1
print("Aramak İstediğiniz Ürün : ")
aranacakKelime= input()

r = requests.get("https://www.hepsiburada.com/ara?q="+str(aranacakKelime))
soup = BeautifulSoup(r.content, "lxml")
sayfa= soup.find_all("div", attrs={"class": "pagination"})[0].find_all("li")
sayfaSayisi = int(sayfa[len(sayfa)-1].text)
print(sayfaSayisi)

for loop in range(1,sayfaSayisi+1):
    r1=requests.get("https://www.hepsiburada.com/ara?q="+str(aranacakKelime)+"&sayfa="+str(loop))
    soup1 = BeautifulSoup(r.content,"lxml")
    products = soup.find_all("p", attrs={"class": "hb-pl-cn"})
    fiyatlar = soup.find_all("span", attrs={"class": "price"})
    for product in range(0, len(products)):
        worksheet.write(satirSayisi, 0, products[product].text)
        worksheet.write(satirSayisi, 1, fiyatlar[product].text)
        satirSayisi=satirSayisi+1
workbook.close()
