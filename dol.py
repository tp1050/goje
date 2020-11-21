import re
import json


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


def loadem():
	#data={}
	# Load the product dictionary
	#with open('tgju.tabaluga') as f:
	#	data = json.load(f)

	#Parse the Raw feed for product proices
	searchfile=open("Feed.htm",encoding="utf-8")
	return  searchfile

def compacter():
	

	searchfile=loadem()
	a=[]

	try:
		for line in searchfile:
			try:
				if "window.source_price" in line: 
					c1=str(re.findall(r"'([^']*)'",line)).replace(']','').replace('[','')
					code1=(c1.replace('\'','')).split(',')
					a.append(code1)
			except Exception as e:
				print (e)
	except Exception as e:
		pass
	searchfile.close()
	return a
	
