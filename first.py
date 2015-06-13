#Ex: Simple Program-------
print("Hey kumar welcom to python.")
print("kumar's lappy")
#print('kumar's lappy')--------occure error during run time because compiler can't understand the starting and ending quotes
print('kumar\'s lappy')   #bypass the single quotes
print("""kumar's lappy""")  #Strictly check
#print(""""kumar's lappy"""") : Error --------occure during run time because it strictly chek the string

#EXp :2
print("-------Example 2: Numbers and Module Function----------------")
print("Addition")
print(2+2)

print("Subtraction")
print(9-5)

print("Division")
print(18/3)

print("Multiplication")
print(5*4)

print("Modulus operation")
print(9%4)

print("Exponent")
print(8**3)

print(9+5*2)
print(3+(4*5))
print((3+4)*5)
print(18%4)
print(18/4)
print("floor the decimal value")
print(18//4)


print("Variable")
x=18
print(x)
print(x+15)
print(x*5)



print("Input variable")
g=input("Enter the any number: ")
print(g)
print(g*3)
h=input("Enter the second number: ")
print(h)
print(g+h)

print("Module and function")
print(5**4)
print(pow(5,4))
print(abs(-15))

print("Using module and function")
#print(floor(18.5))   : Error occure 
import math
print(math.floor(18.5))
print(math.sqrt(81))
x=math.sqrt
print(x(9))


print("----String Concatination-------------")
firstname="kumar"
secondname="gaurav"
print(firstname+" "+secondname)
print(firstname * 5)

print("----------String  Slicing----------")
a="kumar gaurav"
print(a[1])
print(a[-1])
print(a[2:7])
print(a[:7])
print(a[3:])
print(len('kumar'))


print("-------------Loop & conditional statements---------")
name="kumar"
if name=="kumar":
	print("Hey, welcome to python")

print("---using if and else statement---")
name="kumar"
if name=="kumar":
	print("Hey, welcome to python")
else:
	print("Bye Bye....")

print("-----Nested If Statements-----------")
thing="animal"
animal="cat"
if thing=="animal":
	if animal=="cat":
		print("This is a cat")
	else:
		print("I don't no what this animal is.")
else:
	print("I don't no what this thing is")