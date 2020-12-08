import urllib.request
import time

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import codecs
from bs4 import BeautifulSoup

def cleanJ(j):
	pass
def  getHard(url):
	
	profile = webdriver.FirefoxProfile()
	user_agent = "Some UserAgent String here..."
	#~ proxy_ip = "127.0.0.1"
	#~ proxt_port = "9150"
	#~ profile.set_preference("network.proxy.type", 1)
	#~ profile.set_preference("network.proxy.socks", str(proxy_ip))
	#~ profile.set_preference("network.proxy.socks_port", int(proxt_port))
	#~ profile.set_preference("network.http.use-cache", False)
	profile.update_preferences()
	binary = FirefoxBinary("/usr/bin/firefox")
	driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
	driver.get(url)
	html = driver.page_source
	return html

def getUrl(url):
	print (url)
	page = urllib.request.urlopen(url)
	return page.read()
	
	#~ /*
#~ def getRoot(url):
    #~ # This causes an HTTP request; if your script is running more than,
    #~ # say, once a day, you'd want to cache it yourself.  Make sure you
    #~ # update frequently, though!
    #~ url= urlparse(url).hostname

    #~ psl = PublicSuffixList()
    #~ hostname = psl.privatesuffix(url) 
    #~ return hostname

def benevis(content,path):
		if not path:
		# Write where we standing
			newName=str(getrand())+""+str(getMil())
			file1 = open(newName+".html","a",encoding="utf8") 
			file1.write(content)
			file1.close()
			pass
		else:
			#write to path
			pass
		pass




def getMil():
	return int(round(time.time() * 1000))
def getrand():
	return '000'

#~ print (getRoot("http://www.yahoo.com/doodool"))
