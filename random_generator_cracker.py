#!/bib/bash python
#This script is used to get the period for any random number generator if applicable. Many other have protection
#techniques to protect against leak but sometimes there might not be. ALWAYS all rnadom number generator are 
#indeed periodic in nature but then the output may be modified to make it appear look perodic.
import re
import requests

def extract_number(html):
	number=re.search('<br>(\d+)<br>',html).group(1)		#Use own re.search() to get the rnadom number
	return int(number)

def detect_period(url,session):
	numbers=[]
	while True:
		html=session.get(url).text
		number=exract_number(html)
		if number in numbers:
			print 'Found Period:'+str(len(numbers))
			break
		numbers.append(number)
	index=number.index(number)
	return numbers[index:]

if __name__ == '__main__':
	numbers_count=20					#No of predictable guess needed.
	url='http://IP:port/?no=12345'				#URL to check
	session=requests.session()
	numbers=detect_period(url,session)
	print 'Cookie is:'+session.cookies['<name of the cookie>']
	print 'NEXT () NUMBERS ARE:'.format(numbers_count)
	for i in range(numbers_count):
		print numbers[i]

