
#implementing  encapsulation 
class Doctor:
	def __init__(self):
		self.update()
	def cough(self):
		print 'take flugone'
	def typhoid(self):
		print "go for blood test"		
	def update(self):
		print "please"
child=Doctor()
child.cough()
