class Person:
	def __init__(self,name,id,address):   #this self refers to the current object
		self.name=name
		self.id=id
		self.address=address
	
	def printname(self):
		print "name is =" + self.name

	
class Session(Person):
	def __init__(self,name):
		self.name=name
	
	def pythontr(self):
		print "Innovation with python Training"
		
		
res=Person("RIZ")
res.printname()

Res1=Session("RIYAZ")
Res1.printname()
Res1.pythontr()


1: How to write a class
2: How to creat an object of that class
3: What is the use of __init__
4: what is self - Reflection to the current object
5: __str__
6: before commit
7:before commit
8:after clone



