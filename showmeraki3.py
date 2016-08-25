#!/usr/bin/env python

#------------------------------------------------------------------------------------
	# apikeys is a .py file that is in the same directory as this script. setup is meraki="your api key"
import requests
import apikeys
from pprint import pprint

key = apikeys.meraki
url = "https://n49.meraki.com/api/v0/"

main = input("What main function API are you calling? ")
net = input("For what organization or network? " )
info = input("What information are you looking for? ")

headers = {
    'X-Cisco-Meraki-API-Key': key,
    'Content-Type': 'application/json',
}

r=requests.get(url + main + net + info, headers=headers)
r.json()
pprint (r.json())