#!/usr/local/bin/python3

#------------------------------------------------------------------------------------
	# apikeys is a .py file that is in the same directory as this script. setup is meraki="your api key"
import requests, sys, os, argparse, apikeys
from pprint import pprint

progVersion = str('alpha 0.1')


#TODO: refactor to make this less kludgey and more Pep 8 compliant
#TODO: (https://www.python.org/dev/peps/pep-0008/)

global key
global url
global headers

key = apikeys.meraki
url = "https://n49.meraki.com/api/v0/"
headers = {
    'X-Cisco-Meraki-API-Key': key,
    'Content-Type': 'application/json',
    }

def printRequest(_url, main, net, info):
	r=requests.get(_url + main + net + info, headers=headers)
	r.json()
	pprint (r.json())

def saveRequest(_url, main, net, info):
	r=requests.get(_url + main + net + info, headers=headers)
	with open('stuffFile', 'w') as ourFile:
		ourFile.write(mainThings)
		ourFile.write(netThings)
		ourFile.write(infoThings)

def getStuff():
	stuffs = []
	main = input("What main function API are you calling? ")
	net = input("For what organization or network? " )
	info = input("What information are you looking for? ")
	stuffs.append(main)
	stuffs.append(net)
	stuffs.append(info)
	return(stuffs)

def main():
	parser = argparse.ArgumentParser(description='Meraki (enterprise grade) grabber of stuff', epilog='For questions, talk to @wifijanitor')
	parser.add_argument('-d', '--display', action='store_true', dest='displayStuff', help='Display results to screen')
	parser.add_argument('-s', '--save', action='store_true', dest='saveStuff', help='Save results to file')
	commands = parser.parse_args()
	if commands.displayStuff:
		try:
			stuffs = getStuff()
			print(stuffs)
			mainThings = stuffs[0]
			netThings = stuffs[1]
			infoThings = stuffs[2]
			printRequest(url, mainThings, netThings, infoThings)
		except (SystemExit):
			raise
		except (KeyboardInterrupt):
			logging.exception
	elif commands.saveStuff:
		try:
			stuffs = getStuff()
			mainThings = stuffs[0]
			netThings = stuffs[1]
			infoThings = stuffs[2]
			saveRequest(url, mainThings, netThings, infoThings)
		except (SystemExit):
			raise
		except (KeyboardInterrupt):
			logging.exception

if __name__ == '__main__':
	main()

else: print("loaded as module, api, or Skynet...")
