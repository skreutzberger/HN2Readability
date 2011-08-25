#!/usr/bin/env python

# setup asks for the input of user credentials 
# to set the XAuth tokens

import os, sys, readability
from modules import parser

# get the API Keys
keysFile = "data/apikeys.json"
keys = parser.getSettings(keysFile)
if keys == False:
	print ("No developer keys existing in apikeys.json. Please contact Readability to get your own developer keys.")
	sys.exit(0)

# ask for credentials
print	("Welcome to HN2Readability. ")
print ("Please enter your Readability credentials. They will NOT be stored and just used once.")
	
credentials = False
while credentials == False:
	# input of key and secret
	inpUser= "";
	while len(inpUser) < 2:
		inpUser = raw_input("Your Readability username: ")
		
	inpPwd = "";
	while len(inpPwd) < 2:
		inpPwd = raw_input("Your Readability password: ")

	print ("Connecting to Readability to verify your credentials...")
	connected = False
	try:
		token = readability.xauth(keys["consumerKey"], keys["consumerSecret"], inpUser, inpPwd) 
		connected = True
	except:
		print("Wrong credentials, please try again.")	
		
	# load settings 
	if connected:
		settingsFile = "data/settings.json"
		settings = parser.getSettings(settingsFile)

		if settings == False: # assign new preset settings
			settings = {}
			settings['title'] = '' # the last parsed title
			settings['kindle'] = False # directly send to Kindle
	
		settings['token1'] = token[0]
		settings['token2'] = token[1]
		
		# do a connection test with the new token
		try:
			rdd = readability.oauth(keys["consumerKey"], keys["consumerSecret"], token=token)
			me = rdd.get_me()
			credentials = True
		except:
			pass

# finally save all optionally changed settings
parser.saveSettings(settings, settingsFile)

print("Verification successful!")
print("You can now run ./hn2readability.py manually or as a daily cronjob to send the latest Hacker News links to your Readability account.")