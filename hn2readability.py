#!/usr/bin/env python

# the script connects to daemonology and parses the links of the latest day
# and sends them to Readability
import os, sys, readability
from modules import parser

# get the API Keys
keysFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/apikeys.json")
keys = parser.getSettings(keysFile)
if keys == False:
	print ("No developer keys existing in apikeys.json. Please contact Readability to get your own developer keys.")
	sys.exit(0)

# load settings
settingsFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/settings.json")
settings = parser.getSettings(settingsFile) 
if settings == False or not settings['token1'] or not settings['token2']:
	print ("No Readability credentials existing. Please run ./setup.py")
	sys.exit(0)	

# do a connection test with the tokens
print ("Connecting to Readability to verify your token...")
token = (settings["token1"], settings["token2"])
connected = False
try:
	rdd = readability.oauth(keys["consumerKey"], keys["consumerSecret"], token=token)
	me = rdd.get_me()
	connected = True
except:
	pass

if not connected:
	print ("Your Readability credentials seem wrong. Please run ./setup.py")
	sys.exit(0)	
print("Verification successful!")


# returns the html or false of a page
url = 'http://www.daemonology.net/hn-daily/'
fakeConnection = False # True for using data/fakehtml.txt instead of connecting

if fakeConnection:
	html = parser.getFile("data/fakehtml.txt")
else:
	html = parser.getHTML(url)

if html == False:
	print ("Could not connect to ", url)
	sys.exit(0)
	
	
##############
# parse html
# take the first block (the most recent day)
blocks = html.split('<h2>')
block = blocks[1]
title = block.split("</h2>")[0]
# date = title.split("Daily Hacker News for ")[1]

# get the story links
links = []
parts = block.split('<span class="storylink"><a href="')[1:]
for part in parts:
	url = part.split('">')[0]
	if "http" in url and "//news.ycombinator.com" not in url:
		links.append(url)

# was everyhing successfully extracted?
if len(title) < 5 or len(links) < 1:
	print ("Could not extract title and links from page")
	sys.exit(0)


# title was already processed then stop
if settings['title'] == title:
	print ("No new articles today.")
	sys.exit(0)

##############
# send each link to Readability
error = False
counter = 0
for link in links:
	#print("trying to send link " + link)
	try: # fails if article already existing
		response = rdd.add_bookmark(link)
		counter = counter +1
	except:
		error = True

if not error:
	settings['title'] = title # try not again for today anymore
	print("Successfully sent " + str(counter) + " links to Readability")
else:
	print("An error did occur or today's articles were already sent to Readability. Please try again tomorrow.")	
	
# finally save all optionally changed settings
parser.saveSettings(settings, settingsFile)

