import mysql.connector as mysql 


class Anbar:

	db=mysql.connect( host = "localhost", user = "d2", passwd = "22111357")
	cursor = db.cursor()
	def __init__(self):
		pass
	def begir(self,arg):
		try:
			self.cursor.execute(arg)
			return self.cursor.fetchall() ## it returns a list of all databases present
		except Exception as e:       
			print (e)
			return
		pass
	def getCurrencyID(self,arg):
		self.begir("use price_db")
		stmt=" select id from Jens where code='{}' limit 1;".format(arg)
		print (stmt)
		try:
			return self.begir(stmt)[0][0]
		except : 
			return -1
	def getSrcID(self,srcurl):
		#Extract domain name
		#root=Khadang,getRoot(srcurl)
		#self.begir("use price_db")
		#stmt=" select id from Sources where name='{}' limit 1;".format(root)
		#print (stmt)
		#try:
			#return self.begir(stmt)[0][0]
		
	def getRosetaByURL(self,cursor,url):
		#cursor.excute("select ID from Sources")
		#ros=cursor.fetchall()
		return ""
	def bezar
