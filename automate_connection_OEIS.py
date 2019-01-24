#!/bin/bash python
#This script is to auto connect to site http://oeis.org which is used to crack integer sequences. We wrote a script to automate the connection and
#finding the next predicatble sequence and sending it back to server.
from pwn import *
import requests
import hashlib
import re

def captch_cracker(IP,port):
	server=remote("IP",port)
	server.recvuntil("=")
	captcha=server.recvuntil(':')[:-1]
	i=0
	while True:
		i=i+1
		md5str=hashlib.md5(str(i)).hexdigest()
		if captcha==mad5str:
			print "Captcha found: %i" %i
			break
	server.sendline(str(i))

for i in range(0,25):
	server.readuntil("[")
	numbers_sequence=r.readuntil("]")[:-1]
	rr=requests.get("oeis.org/search?q="+numbers_sequenece).text
	try:
		number_future=re.search('color:black;font-size:120%;">',rr).group(0)	#regex to match the next numbers
		print "Found sequece: "+number_futur
	except:
		print "Not found in OEIS"
	server.sendline(number_future)

r.interactive()	
