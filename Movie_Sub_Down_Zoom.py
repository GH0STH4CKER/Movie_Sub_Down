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
     [+] Made by GH0STH4CK3R            [+] zoom.lk
 --------------------------------------------------------------"""
print(lG+banner,lY+tag)

print(lG+"")

search = input("Search Movie Subtitle : ")

url = "https://zoom.lk/?s="+search

r = requests.get(url)

page_soup = bSoup(r.text,"html.parser")

html = page_soup.find_all("a")#{"class":"entry-title td-module-title"}) # Made by GHOSTH4CK3R 

linklist = []
Sno = 1

for i in range(len(html)) :
    try:
        title = str(html[i]['title'])
    except Exception as e:
        pass
    else :
        if "(සිංහල උපසිරැසි)" in title :
            if "<img" not in str(html[i]) :
                print("\n")
                print(' [',Sno,'] ',title)
                linklist.append(html[i]['href'])
                Sno += 1

Sub_no = int(input("Enter Subtitle No : "))

url2 = linklist[Sub_no-1]
svnm = str(url2).replace('https://zoom.lk/','')  
svnm = svnm.replace('-%e0%b7%83%e0%b7%92%e0%b6%82%e0%b7%84%e0%b6%bd-%e0%b6%8b%e0%b6%b4%e0%b7%83%e0%b7%92%e0%b6%bb%e0%b7%90%e0%b7%83%e0%b7%92/','')
print("\n You Choosed >> ",'[',Sub_no,'] ',svnm)

r2 = requests.get(url2)

page_soup = bSoup(r2.text,"html.parser")

html2 = page_soup.find_all("a",{"class":"aligncenter download-button"}) 

Down_link = str(html2[0]['href'])

url3 = Down_link
r3 = requests.get(url3)

svnm = svnm+".rar"

if r3.status_code == 200 :
    file = open(svnm, 'wb')
    file.write(r3.content)
    file.close()

    print(lY+"\nFile download success !")
    print(svnm)

else :
    print(lR + "\nDownload Failed ! ",r3.status_code)    


