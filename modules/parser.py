# functions to parse strings, web pages, etc.
import urllib, json


# returns the html of a page or False
def getHTML(source):
	try:
		sock = urllib.urlopen(source) 	
		html = sock.read()                            
		sock.close()   
		return html
	except:
		return False	
		
# returns the content of a file or False		
def getFile(source):
	try:
		f = open(source, "r")
		return f.read()
	except:
		return False		


# returns a dictionary of stored settings or False
def getSettings(settingsFile):
	try: 
		with open(settingsFile, 'r') as f:
			return json.load(f)    
	except:
		return False	


# stores the settings in a json file
# returns boolean on success
# FIXME: issues with special characters!!
def saveSettings(data, settingsFile):
	try:
		with open(settingsFile, 'w') as f:
			json.dump(data, f) 
		return True
	except:
		return False		
