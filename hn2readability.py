#!/usr/bin/env python
##coding: utf-8

import os, sys, readability

##### I M P O R T S #######
from modules import parser

# returns the html or false of a page
url = 'http://www.daemonology.net/hn-daily/'
#html = parser.getHTML(url)

# take html from file
html = parser.getFile("html.txt")

if html == False:
	print ("Could not connect to ", url)
	sys.exit(0)

# take the first block (the most recent day)
blocks = html.split('<h2>')
block = blocks[1]
title = block.split("</h2>")[0]
date = title.split("Daily Hacker News for ")[1]

# get the story links
links = []
parts = block.split('<span class="storylink"><a href="')[1:]
for part in parts:
	url = part.split('">')[0]
	if "http" in url and url != "https://news.ycombinator.com/":
		links.append(url)

# was everyhing successfully extracted?
if len(date) != 10 or len(links) < 1:
	print ("Could not extract date and links from page")
	sys.exit(0)

