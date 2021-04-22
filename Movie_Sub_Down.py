# Python 3.8.3
# Coded By GH0STH4CK3R
import requests , bs4 , time , os
from colorama import Fore , init
from bs4 import BeautifulSoup as bSoup
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
     [+] Made by GH0STH4CK3R            [+] baiscopelk
 --------------------------------------------------------------"""
print(lG+banner,lY+tag)

print(lG+"")
sphrase = input("Search Movie : ")

url1 = "https://www.baiscopelk.com/"

params = {"s": sphrase}

r1 = requests.get(url1,params=params)

if r1.status_code != 200 :
    print(lR+"Make sure you have internet !")
    time.sleep(8)
    exit()

dat = r1.text

data = dat[int(dat.find('Search Results for')):999999]

page_soup = bSoup(data,"html.parser")

html = page_soup.find_all("div",{"class":"post-thumbnail"}) 

imgsrcList = []
ahrefList = [] 
linkl = []
links = []
i = 0

for x in range(len(html)) :
    if "mega-menu-link" in str(html[x]) or "rel=\"bookmark\"" in str(html[x]) or "ttip" in str(html[x]) :
        pass
    else:
        htmldata = str(html[x])
        page_soup1 = bSoup(htmldata,"html.parser")
        hreflink = page_soup1.findAll('a')#[0]['href'] #page_soup.find('MADE BY GH0STH4CK3R')
        if len(hreflink) != 0 :
            i += 1
            links.append(hreflink[0]['href'])
        
print("Displying",i,"Results\n\n")
for y in range(len(links)) :
    link = str(links[y]).replace('https://www.baiscopelk.com/','')
    link = link.replace('/',' ')
    linkl.append(link)
    link = link.replace('-',' ')
    print("[",y+1,"]  ",link,"\n")
#print(ahrefList[0])

print()
n = int(input("Enter No : "))

print("\nYou choosed >> ",linkl[n-1])

url2 = links[n-1]

r2 = requests.get(url2)
data2 = r2.text

page_soup2 = bSoup(data2,"html.parser")

html2 = page_soup2.find_all("a",{"style":"color: #ff3300;"}) 

ziplink = html2[0]['href']


url3 = ziplink#"https://www.baiscopelk.com/Downloads/scooby-doo-the-sword-and-the-scoob-2021-1-zip/ (C) Copyright (R) GH0$TH4CKR"

r3 = requests.get(url3)

if r3.status_code == 200 :
    sv = linkl[n-1]+".zip"
    file = open(sv, "wb")
    file.write(r3.content)
    file.close()

    print(lY+"\nFile download success !")
    print(sv)

else :
    print(lR+"Something went wrong !  Error code ",r3.status_code)    
