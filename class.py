class Avenger:
	avengersCount = 0
	def __init__(self,name,power):
		Avenger.avengersCount += 1
		#self.avengersCount =1
		self.name=name
		self.power=power
	def howMany():
		print("Total Avengers %d" % Avenger.avengersCount)
	def getName(self):
		print("Avengers Name: " +name+ "hav power "+power )

#ironMane = Avengers()
#hulk.avengersCount()
hulk=Avenger("hulk","Angry")
print(hulk.name)
print(hulk.power)
print("AvengersCount: ", Avenger.avengersCount)
print("---------------------------")

ironMan=Avenger("ironMan","suit")
print(ironMan.name)
print(ironMan.power)
print("AvengersCount: ", Avenger.avengersCount)

#print("AvengersCount: ", hulk.avengersCount,ironMan.avengersCount)
print("-------------------Example 3-----------------")
#EXP : 3
class Avenger:
	avengersCount = 0
	def __init__(self,name,power):
		Avenger.avengersCount += 1
		#self.avengersCount =1
		self.name=name
		self.power=power
	def howMany():
		print("Total Avengers %d" % Avenger.avengersCount)
	def getName(self):
		print("Avengers Name: " +self.name+ "hav power "+self.power )

#ironMane = Avengers()
#hulk.avengersCount()
hulk=Avenger("hulk","Angry")
print(hulk.name)
print(hulk.power)
hulk.getName()
Avenger.howMany()
print("AvengersCount: ", Avenger.avengersCount)

print("---------------------------")

ironMan=Avenger("ironMan","suit")
print(ironMan.name)
print(ironMan.power)
print("AvengersCount: ", Avenger.avengersCount)
Avenger.howMany()
ironMan.getName()
Avenger.howMany()

#EXP : 4
print("-----------Example 4---------")
class Fruit:
	fruitsCount = 0
	def __init__(self,name):
		Fruit.fruitsCount +=1
		self.name=name
	def howMany():
		print("Total Fruit : %d" % Fruit.fruitsCount)
	def getName(self):
		print("Fruit name: " +self.name)
x=Fruit("Mango")
x=Fruit("Apple")
x=Fruit("Apricot")
x=Fruit("Banana")
print(x.name)
x.getName()
Fruit.howMany()	
print("--------------------------------")


#EXP :5
print("----------------Example 5----------")
class Avenger:
	avengersCount = 0
	def __init__(self,name,power):
		Avenger.avengersCount += 1
		#self.avengersCount =1
		self.name=name
		self.power=power
	def howMany():
		print("Total Avengers %d" % Avenger.avengersCount)
	def getName(self):
		print("Avengers Name: " +self.name+ "hav power "+self.power )

#ironMane = Avengers()
#hulk.avengersCount()
hulk=Avenger("hulk","Angry")
print(hulk.name)
print(hulk.power)
hulk.getName()
Avenger.howMany()
print("AvengersCount: ", Avenger.avengersCount)

print("---------------------------")

ironMan=Avenger("ironMan","suit")
print(ironMan.name)
print(ironMan.power)
print("AvengersCount: ", Avenger.avengersCount)
Avenger.howMany()
ironMan.getName()
print("")
hulk.size="very big"
print(hulk.size)
del hulk.power
#print(hulk.power)


#print(getattr(hulk,"name"))
x=getattr(hulk,"name")
print(x)
print(setattr(hulk,"name","bada hulk"))
print(hulk.name)