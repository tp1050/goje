import Khadang 
import json

from bs4 import BeautifulSoup


url="https://divar.ir/s/tehran/real-estate"
#get content

content=Khadang.getUrl(url)   
#Khadang.benevis(content,"")
tree = BeautifulSoup(content,"html5lib")
s=tree.findAll('script',{"type":"application/ld+json"})

data=json.loads((s[1]).contents[0])
Khadang.benevis(str((json.dumps(data,ensure_ascii=False).encode('utf8')).decode()),"")
if data:
	Khadang.cleanJ(data,"@context")
	Khadang.cleanJ(data,"accommodationCategory")
	for h in data:
		Khadang.cleanSize(h)
		Khadang.cleanGeo(h)


Khadang.benevis2(data)