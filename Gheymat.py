class Gheymat:
	jensID=0
	srcID=0
	dt=''
	price='0'
	currency=55
	bs=0
	def __init__(self, product=0, src=0, dt='2020-10-10 10:17:26.220921' ,price=0, currency=0,	bs=0):
		 self.src= src
		 self.product=product
		 self.price=price
		 self.currency=currency
		 self.bs=bs
		 self.dt=dt
	def commit(self,arg):
		
		if  isinstance(arg,MySQLCursor):
			pass
		elif :
			Khadang.benevis(begoo(),arg)
		
		pass
		
		
		
	def begoo(self):
		return ("{} claims: {} is sold  at price :{} in currency :{} at time :{}". format (self.src,self.product, self.price,self.currency,self.dt))
