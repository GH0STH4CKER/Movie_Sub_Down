from colorama import Fore , init
from os import system, name
import os
init()

def clear() :
    if name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

lG = Fore.LIGHTGREEN_EX
lR = Fore.LIGHTRED_EX
lY = Fore.LIGHTYELLOW_EX
lC = Fore.LIGHTCYAN_EX

banner = """
  █▀▄▀█ █▀█ █ █ █ █▀▀ ▄▄ █▀ █ █ █▄▄ ▄▄ █▀▄ █▀█ █ █ █ █▄ █
  █ ▀ █ █▄█ ▀▄▀ █ ██▄    ▄█ █▄█ █▄█    █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ V1.0"""
tag = """
 ______________________________________________________________
                    [+] Made by GH0STH4CK3R         
 --------------------------------------------------------------"""
print(lG+banner,lY+tag)

print(lG+"")


lang = input("What Language you want ? \n\n[S] Sinhala\n[E] English\n")

if lang == "s" or lang == "S" :
    choice = int(input("Website you want to download subtitles ? \n\n[1] Baiscopelk.com\n[2] Zoom.lk \n\nChoose >> \n"))
    if choice == 1 :
        clear()
        import bin.Movie_Sub_Down_Baiscope
    elif choice == 2 :
        clear()
        import bin.Movie_Sub_Down_Zoom
    else :
        print(lR+"Wrong choice !")

elif lang == "e" or lang == "E" :
	clear()
	import bin.Movie_Sub_Down_Yts
else :
	print(lR+"Wrong Language !")



