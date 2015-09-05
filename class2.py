#class Github(Object):
#	def __init__(self,members):
#		self.members =members
#		self.code=code

#class Dinesh-sunny(Github):
#	def __init__():
#		super(Github.__init__())

#tuple is use for referece and update the value in a list.

print("-----------enemy class example-----------")
class Enemy:
	life=3
	def attack(self):
		print("OOPs....")
		self.life -=1

	def checkLife(self):
		if self.life<=0:
			print("You are dead.")
		else:
			print(str(self.life)+ " left life")


enemy1=Enemy()
enemy1.attack()
enemy1.checkLife()

enemy2=Enemy()
enemy2.attack()
enemy2.checkLife()
  
enemy3=Enemy()
enemy3.attack()
enemy3.checkLife()

