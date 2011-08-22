# functions to parse strings, web pages, etc.
import urllib
# returns the html or false of a page
def getHTML(source):
	try:
		sock = urllib.urlopen(source) 	
		html = sock.read()                            
		sock.close()   
		return html
	except:
		return False	
		
# returns the content of a file or false		
def getFile(source):
	try:
		f = open(source, "r")
		return f.read()
	except:
		return False		
