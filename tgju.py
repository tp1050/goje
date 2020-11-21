import re
from datetime import datetime
from Gheymat import Gheymat
from Anbar import Anbar

src_url="https://www.tgju.org/"
proxy_req=0
# Load the Product Dictionary  L:SRC R:DBsymb
data={

"price_dollar_rl":"USDREAL",
"price_dollar_realtime":"USDREAL",
"sekee":"sekee",
"sekeb":"sekeb",
"rob":"robseke",
"nim":"nimseke",
"gerami":"sekeg",
"btc-irr":"btc",
"eth-irr":"eth",
"dash-irr":"dash",
"xrp-irr":"xrp",
"eos-irr":"eos",
"xlm-irr":"xlm",
"usdt-irr":"usdex"

}
def getPriceFromLine(line):
	try:
		if "window.source_price" in line: 
			c1=(str(re.findall(r"'([^']*)'",line)).replace(']','').replace('[','') )
			code1=c1.replace('\'','').split(',')
			if code1[1] :
				return code1
	except Exception as e:
		pass 
	

def loadRaw():
	return open("index.html",encoding="utf-8").readlines()

def getPrice():
	a=[]
	
	try:
		for line in loadRaw():
			an=Anbar()
			temp=getPriceFromLine(line)
			gh= Gheymat()
			if temp:
				gh.product= an.getCurrencyID (data[temp[0]])
				gh.price=temp[1]
				gh.currency=an.getCurrencyID ('IRR')
				a.append(gh)
	except Exception as e:
		print (e)	
	return a
	
