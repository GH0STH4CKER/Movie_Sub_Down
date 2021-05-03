# Python 3.8.3
# (C) Coded By GH0STH4CK3R
import requests , bs4
from bs4 import BeautifulSoup as bSoup
from colorama import Fore , init

init()
lG = Fore.LIGHTGREEN_EX
lR = Fore.LIGHTRED_EX
lY = Fore.LIGHTYELLOW_EX
lC = Fore.LIGHTCYAN_EX

banner = """
  █▀▄▀█ █▀█ █ █ █ █▀▀ ▄▄ █▀ █ █ █▄▄ ▄▄ █▀▄ █▀█ █ █ █ █▄ █
  █ ▀ █ █▄█ ▀▄▀ █ ██▄    ▄█ █▄█ █▄█    █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ V1.0"""
tag = """
 ______________________________________________________________
     [+] Made by GH0STH4CK3R            [+] yts-subs.com
 --------------------------------------------------------------"""
print(lG+banner,lY+tag)

print(lG+"")
search = input("Search Movie Subtitle : ")
search = search.replace(' ','%20')

url = "https://yts-subs.com/search/"+search

r = requests.get(url)

page_soup = bSoup(r.text,"html.parser")

h3tag = page_soup.find_all("h3",{"class":"media-heading"}) # Made by GHOSTH4CK3R 
n = 1
n2 = 1
links = []
links2 = []
links3 = []
langs = []

for i in h3tag :
    title = i.text.strip()
    print(' [',n,'] ',title)
    n += 1

for tag in page_soup.find_all('div', {'class' : 'media-body'}):
    for anchor in tag.find_all('a'):
        links.append('https://yts-subs.com'+anchor['href'])

sch1 = int(input("\nEnter Movie No : "))
url2 = links[sch1-1]

r2 = requests.get(url2)

page_soup = bSoup(r2.text,"html.parser")


for trtag in page_soup.find_all('tr', {'class' : 'high-rating'}):
    for anchor2 in trtag.find_all('a'):
        shortlink = str(anchor2['href'])
        if 'english' in shortlink :
            subname = str(anchor2.text.strip())
            subname = subname.replace(' ','')
            subname = subname.replace('download','')
            salpha = subname.replace(' ','')
            if salpha != '' :
                links2.append('https://yts-subs.com'+shortlink)
                print(' [',n2,'] ENGLISH \n',subname)
                n2 += 1
            
sch2 = int(input("\nEnter Subtitle no : "))
url3 = links2[sch2 -1]        

r3 = requests.get(url3)
page_soup = bSoup(r3.text,"html.parser")
downtag = page_soup.find_all("a",{"class":"btn-icon download-subtitle"})

zipdownlink = downtag[0]['href']

url4 = zipdownlink
r4 = requests.get(url3)

svnm = str(url4).replace('https://yifysubtitles.org/subtitle/','')
#print(svnm)

if r4.status_code == 200 :
    file = open(svnm, 'wb')
    file.write(r4.content)
    file.close()

    print(lY+"\nFile download success !")
    print(svnm)

else :
    print(lR + "\nDownload Failed ! ",r4.status_code)    

input("\n\nExit >")