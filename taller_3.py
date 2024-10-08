import bs4 as bs 
import urllib.request

enlace = "https://es.wikipedia.org/wiki/Canis_familiaris"
enlace1 = "https://es.wikipedia.org/wiki/Canis_lupus"
enlace2 = "https://es.wikipedia.org/wiki/Delphinidae"
enlace3 = "https://es.wikipedia.org/wiki/Oryctolagus_cuniculus"
enlace4 = "https://es.wikipedia.org/wiki/Psittacoidea"
enlace5 = "https://es.wikipedia.org/wiki/Struthio_camelus"
enlace6 = "https://es.wikipedia.org/wiki/Elephantidae"
enlace7 = "https://es.wikipedia.org/wiki/Gorilla"
enlace8 = "https://es.wikipedia.org/wiki/Panthera_pardus"
enlace9 = "https://es.wikipedia.org/wiki/Giraffa_camelopardalis"

link = [enlace, enlace1, enlace2, enlace3, enlace4, enlace5, enlace6, enlace7, enlace8, enlace9]

request = urllib.request.Request(enlace, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(request)
source = webpage.read()
webpage.close()
soup = bs.BeautifulSoup(source, 'html.parser')

request1 = urllib.request.Request(enlace1, headers={'User-Agent': 'Mozilla/5.0'})
webpage1 = urllib.request.urlopen(request1)
source1 = webpage1.read()
webpage1.close()
soup1 = bs.BeautifulSoup(source1, 'html.parser')

request2= urllib.request.Request(enlace2, headers={'User-Agent': 'Mozilla/5.0'})
webpage2 = urllib.request.urlopen(request2)
source2 = webpage2.read()
webpage2.close()
soup2 = bs.BeautifulSoup(source2, 'html.parser')

request3 = urllib.request.Request(enlace3, headers={'User-Agent': 'Mozilla/5.0'})
webpage3 = urllib.request.urlopen(request3)
source3 = webpage3.read()
webpage3.close()
soup3 = bs.BeautifulSoup(source3, 'html.parser')

request4 = urllib.request.Request(enlace4, headers={'User-Agent': 'Mozilla/5.0'})
webpage4 = urllib.request.urlopen(request4)
source4 = webpage4.read()
webpage4.close()
soup4 = bs.BeautifulSoup(source4, 'html.parser')

request5 = urllib.request.Request(enlace5, headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urllib.request.urlopen(request5)
source5 = webpage5.read()
webpage5.close()
soup5 = bs.BeautifulSoup(source5, 'html.parser')

request6 = urllib.request.Request(enlace6, headers={'User-Agent': 'Mozilla/5.0'})
webpage6 = urllib.request.urlopen(request6)
source6 = webpage6.read()
webpage6.close()
soup6 = bs.BeautifulSoup(source6, 'html.parser')

request7 = urllib.request.Request(enlace7, headers={'User-Agent': 'Mozilla/5.0'})
webpage7 = urllib.request.urlopen(request7)
source7 = webpage7.read()
webpage7.close()
soup7 = bs.BeautifulSoup(source7, 'html.parser')

request8 = urllib.request.Request(enlace8, headers={'User-Agent': 'Mozilla/5.0'})
webpage8 = urllib.request.urlopen(request8)
source8 = webpage8.read()
webpage8.close()
soup8 = bs.BeautifulSoup(source8, 'html.parser')

request9 = urllib.request.Request(enlace9, headers={'User-Agent': 'Mozilla/5.0'})
webpage9 = urllib.request.urlopen(request9)
source9 = webpage9.read()
webpage9.close()
soup9 = bs.BeautifulSoup(source9, 'html.parser')

soup_list = [soup, soup1, soup2, soup3, soup4, soup5, soup6, soup7, soup8, soup9]

for i in soup_list:
    print(i.find("h1").contents)



for i in soup_list:
    print(i.find("tbody").find("p").contents)



    





