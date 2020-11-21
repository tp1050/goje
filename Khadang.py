from publicsuffixlist import PublicSuffixList
import time

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


def getRosetaByURL(self,cursor,url):
	cursor.excute("select ID from Sources;")
	ros=cursor.fetchall()
	return ""



def getRoot(url):
    # This causes an HTTP request; if your script is running more than,
    # say, once a day, you'd want to cache it yourself.  Make sure you
    # update frequently, though!
    url= urlparse(url).hostname

    psl = PublicSuffixList()
    hostname = psl.privatesuffix(url) 
    return hostname

def benevis(self,content,path):
	if len(path) <= 1
		# Write where we standing
			file1 = open( getrand+getMil,"a") 
			pass
		else:
			#write to path
			pass
	pass



def getMIl():
	return int(round(time.time() * 1000))
def getRand():
	return '000'

print (getRoot("http://www.yahoo.com/doodool"))