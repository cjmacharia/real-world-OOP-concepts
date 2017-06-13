
#implementing  encapsulation 
class Doctor:
	def __init__(self):
		self.update()
	def cough(self):
		print 'take flugone'
	def typhoid(self):
		print "go for blood test"		
	def update(self):
		print "get tested"


# implementing inheritance the nurse is inheriting from the doctor 

class Nurse(Doctor):
	def __init__(self):
		self.getPatient()
	def medicine():
		pass
	def getPatient():
		pass			
	