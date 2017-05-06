#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
Türk-Altay Linux Sürümü (v1.0)
"""

__projectAuthor = "Keylo99"
__PyAuthor__    = "Black Viking"
__date__        = "06.05.2017"


import os
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append("./source")

import dorkMaker
import dorkScanner
import bruteForce

def logo():
	print """
___________            __                _____  .__   __                
\__    ___/_ _________|  | __           /  _  \ |  |_/  |______  ___.__.
  |    | |  |  \_  __ \  |/ /  ______  /  /_\  \|  |\   __\__  \<   |  |
  |    | |  |  /|  | \/    <  /_____/ /    |    \  |_|  |  / __ \\___   |
  |____| |____/ |__|  |__|_ \         \____|__  /____/__| (____  / ____|
                           \/                 \/               \/\/     

\t\t\t\t\tVersion 1.0.0
\t\t\t\t\tBlack Viking - Keylo99
\t\t\t\t\thttp://github.com/blackvkng"""

def menu():
	print """
\t\t[1] Dork Maker
\t\t[2] Brute Force
\t\t[3] SQLi Scanner
\t\t[3] Dork Scanner\n"""

def altayDork():
	while True:
		dork = raw_input("altay (dorkMaker) => ").decode(sys.stdin.encoding or 'utf-8')

		if dork == "yardım":
			altayDorkHelp()

		elif dork == "geri":
			break

		elif dork == "dorkları göster":
			if len(dorkMaker.dorks) != 0:
				print "-"*60
				for dork in dorkMaker.dorks:
					print "  "+dork
				print "-"*60
				print "[*] Listede %s dork var!"%(len(dorkMaker.dorks))

		elif "dork üret" in dork:
			try:
				num = int(dork.split()[-1])
			except ValueError:
				print "[-] Örnek kullanım: dork üret 10"
				altayDork()
				
			dorkMaker.dorks = []
			dorkMaker.generateDork(int(raw_input("[*] Kaç adet WordPress dork üretilsin: ")))
			print "[+] %s dork üretildi!"%(len(dorkMaker.dorks))

def bruteForce():

def main():
	while True:
		altay = raw_input("\naltay => ").lower()

		if altay == "help":
			help()

		elif altay == "exit":
			sys.exit()

		elif altay == "clear":
			clear()

		elif altay == "1":
			altayDork()



if __name__ == '__main__':
	logo()
	menu()
	main()
