#!/bin/bash python
#Script to brute force captcha which compares input with random MD5 hash so 
#we take number i.e 1 and so on and compute their MD5 and compare with that of
#server and crack the hash.
from pwn import *
import hashlib

server=remote("IP",port)

server.recvuntil("=")
captcha=server.recvuntil(".")[:-1]
i=0
while True:
	i+=1
	md5str=hashlib.md5(str(i)).hexdigest()
	if md5str==captcha:
		print "Found captcha %i" %i
		break

server.sendline(str(i))
