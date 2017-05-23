#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
dorkMaker.py, generate dorks for Wordpress.

Usage:
	~$ python2 dorkMaker.py 100

	// 100 dork will be here
"""

__author__ = "Black Viking"
__date__   = "16.04.2017"

import re
import sys
import ragent
import random
import requests


wordPressDorks = [
	'("Just another WordPress site")', 
	'("Comment on Hello world!")', 
	'("Mr WordPress on Hello world!")', 
	'("uncategorized")', 
	'("author/admin")'
				]

wordsSite = "https://randomword.com/"
dorks     = []

def getRandomWord():
	''' Get random words '''

	header = {'User-agent': ragent.ua()}

	req  = requests.get(url=wordsSite, headers=header)
	word = re.findall('<div id="random_word">(.*?)</div>', req.text)[0]

	return word

def generateDork(x):
	''' Generate Dorks'''

	for i in range(1, int(x)+1):
		dork = random.choice(wordPressDorks) + getRandomWord()
		dorks.append(dork)

	return dorks

if __name__ == "__main__":
	''' When script runs directly '''

	if len(sys.argv) == 2:
		print "\n" + "-"*60
		for dork in generateDork(sys.argv[1]):
			print dork
		print "\n" + "-"*60
		print "\n[+] %s dork generated!"%(len(dorks))

	else:
		sys.exit()
