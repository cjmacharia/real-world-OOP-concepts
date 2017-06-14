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

# implementing inheritance the nurse is inheriting from the doctor 

class Nurse(Doctor):


	def __init__(self):
		self.getPatient()
		
	def medicine():
		pass
		
	def getPatient():
		pass
		
"""		
implementing polymophism We create two classes 
  patientOne and patientTwo, 
  We then make two instances and call their action using the same method """"  
  
class patientOne(object):


	def prescription(self):
		print "take 1*3"
		
class patientTwo(object):


	def prescription(self):
		print "take 3*3"

def getPrescription(pType):
	pType.prescription()

pOne=patientOne()
pTwo=patientTwo()

getPrescription(pOne)
getPrescription(pTwo)