import codecs
from bs4 import BeautifulSoup

html=open("a.html", "r").read()

tree = BeautifulSoup(html,"html5lib")
s=tree.findAll('td',{"class":"same_val"})
aaa=""
aa=""
for i in s:
	print i
	aa=aa+"\n"+str(i).replace("<td class=","").replace("same_val","").replace("id","")
	
print type(tree)
print 1
file_object = codecs.open("ar.html", "w", "utf-8")
file_object.write( aa)
file_object.close()
#ile_object.write(html)
#tdUsd = driver.find_element_by_id("usd1")

#driver.save_screenshot("check_ip.png")