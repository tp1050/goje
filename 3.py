import json
import Khadang
import mysql.connector


db=mysql.connector.connect( host = "localhost", user = "root", passwd = "22111357")
cursor = db.cursor()

with open('q.html', encoding='utf-8') as fh:
    data = json.load(fh)
if data:
	#Khadang.cleanJ(data,"@context")
	#Khadang.cleanJ(data,"accommodationCategory")
	#for h in data:
	#	Khadang.cleanSize(h)
	#	Khadang.cleanGeo(h)



x=json.dumps(data,ensure_ascii=False).encode('utf8')
print (x.decode())
Khadang.benevis2(x.decode())

k=(
"INSERT INTO 'moozmar'.'agahi_melk'"
"('address',"
"'accommodationCategory',"
"'category',"

"'description',"
"'floorSize',"
"'geo',"
"'image',"
"'name',"
"'numberOfRooms',"
"'offers',"
"'type',"
"'url') "
"VALUES "

"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s),"
"(%s));")
#print ( k)

