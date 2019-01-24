#!/bin/bash python
#We have increment,multiplier,modulus all unkown but we get their values using the random numbers generated
#This is script to crack LCD radom number generator. Refer:https://tailcall.net/blog/cracking-randomness-lcgs/
#increment = m,multiplier=c,modulus=n
import re
import requests

from gmpy2 import gcd, invert
from functools import reduce

url='http://IP:port/?guess={}'
recover_size=10
streak_count=20

class LCG:
	def __init__(self, m, a, c, seed):
		self.m=m
		self.a=a
		self.c=c
		self.state=seed

	def next(self):
		self.state=(self.a * self.state + self.c) % self.m
		return self.state

def crack_unknown_increment(states,modulus,multiplier):
	increment=(states[1] - states[0]*multiplier) % modulus
	return modulus, multiplier, increment

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def recover_lcg(session):
	numbers=[]
	for i in range(recover_size):
		html=sesion.get(url.format(1)).text
		number=re.search('<br>(\d+)<br>',html).group(1)
		numbers.append(number)
	modulus,multiplier,increment=crack_unkown_modulus(numbers)
	lcg=LCG(modulus, multiplier, increment, numbers[-1])
	return lcg

def obtain_flag(lcg,session):
	numbers=[lcg.next() for i in range(streak_count)]
	for number in numbers:
		html=session.get(url.format(number)).text
		match=re.search('X-MAS\{.*?\}',html)
		if match:
			return match.group(0)

if __name__ == '__main__':
	session=requests.session()
	lcg=recover_lcg(session)
	print('modulus={}, multiplier={}, increment={}'.format(lcg.m, lcg.a, lcg.c))
    	flag = obtain_flag(lcg, session)
	print(flag)
