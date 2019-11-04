import requests
from bs4 import BeautifulSoup

url = "https://kur.doviz.com/"

html = requests.get(url).content    
soup = BeautifulSoup(html, "html.parser")

items = soup.find("div", {"class":"table"}).find_all("tr")

dovName = []
i=True
exchane = {}
for info in items:
    name = info.get('data-table-subpage-key')
    
    if i == True or name == None:
        i=False
        continue
    
    value = info.find_all("td")[2].text.replace(",",".")
    value = float(value)
    exchane[name] = value
    dovName.append(name)
print('******************************************\n')
print("döviz tipleri : ")
print(dovName)
bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz  = input("alinan döviz türü: ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))
print('\n*******')
if bozulan_doviz == 'TRY':
    temp = miktar / exchane[alinan_doviz]
    temp2= 1/exchane[alinan_doviz]
    
elif alinan_doviz == 'TRY':
    temp = exchane[bozulan_doviz] * miktar
    temp2 = exchane[bozulan_doviz]

else:
    temp = exchane[bozulan_doviz] * miktar
    temp = temp /exchane[alinan_doviz]
    temp2 = exchane[bozulan_doviz] / exchane[alinan_doviz]

print("1 {} = {:.4f} {}".format(bozulan_doviz,temp2,alinan_doviz))
print(f"{miktar} {bozulan_doviz} = {temp:.4f} {alinan_doviz}")
print('*******')
print('\n******************************************')   

