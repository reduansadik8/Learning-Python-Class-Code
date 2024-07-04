#we use # to make a note or to comment out
#Machine -------> Translator ---------> Code
#Code --------> Translator ----------> Machine
#We can press ctrl + /  to make a muktiple line comment at once



# What is Python ?
# >Python is simple and easy
# >Pree and open Source
# >High Level Language
# >Developed by Guido van Rossum
# >Portable to tone operating system to another



#Our first Program
#We use "" between ( ) to print the text that is in the ( )

print("Hello World")
print("MD Redeuanul Hoque")
print("My Name is Sadik")
print("Apna College")

#We use Ctrl + S to save a life or a folder



# Python Character set
# > Letters - A to Z , a to z
# > Digits - 0 to 9
# > Special Symbols - & $ @ / etc.
# > Whitespaces - Blank Space , tab , carriage return , newline, formfed
# > Other Characters - Python can process allASCII and Unicode
# characters as part of data or literals



print("Apna College")
print("My age is 20")
print("23")
print("23+58")
print("58-20")
print("2*30")
print("30/2")



# Varriables
# A variable is a name given to a memory location in a program.
#Variable = Value
name = 'Sadiik'
age = 32
GPA = 5.00

print(name)
print(age)
print(GPA)

#We never use "" between ( ) to print a value of a variable.
#we just put the variable name between ( )



# Rules for Identifiers/Variables 
# > Identifiers can be combination of uppercase and lowercase letters , digits,
# or an underscore(_). So myvariable_1,variable_for_print all are valid python 
# identifiers or variables.
# > An identfier can not start with digit. So, while variable1 is valid , 
# 1variable is invalid.
# >We can not use special symbols like ! # @ $ etc in out identifier.
# >Identifier can be of any length
# > Identifiers can not contain space


# Data Types
# > Integers
# > String
# > float
# > Boolean
# > None
 
#String : It is a name or a scentance that is covered be " " 

name = "sadik"
name1 = "My name is Sadik"

print(name)
print(name1)

#Integers : It is mainly numbers from minus infinity to plus infinity including 0

roll = 26
age = 20

print(roll)
print(age)

#Float : It is also a type of number but it contains decimal

price = 25.50
run_rate = 7.89

print(price)
print(run_rate)

#Boolean : Boolean value can eigther True or False

a = 23
b = 25

print(a>b)
print(a<b)



#Type identification : print(type(variable name))

name = "MD Reduanul Hoque"
age = 23
run_rate = 10.91
old = False
bad_habbit = None

print(type(name))
print(type(age))
print(type(run_rate))
print(type(old))
print(type(bad_habbit))



#Keywords : Keywords are reserved words in python we can not use them as
# variavle name

#Example : and , as , else , except , in , is , return , 
# False , True , None, lambda , while, continue , finally etc.



# Types of Operators

# > Arithmetic Operators ( + - * / % **)

# > Relational / Comarison Operators ( == != > < >= <= )

# > Assignment Operators (= += -= *= /= %= **=)

# > Logical Operators (not , and , or)

# Arithmetic Operators 

#print sum

a = 5 
b = 10
sum = a + b
print(sum)

#print difference
a = 10
b = 6
diff = a - b
print(diff)

#print multiplication 
a = 3
b = 4
mult = a*b
print(mult) 

#Print Division 
a = 90
b = 2
div = a/b
print(div)

#print remainder
a = 10
b = 3
rem = a % b
print(rem)

#print power
a = 5
b = 2
pow = a ** b
print(pow)


# Rational / Comparison Operators : Answer will be True or False

#Is a = b ?

a = 20 
b = 20 
print(a==b)

a = 20
b = 30
print(a==b)

#Is a not wquals to b ?

a = 20
b = 30
print(a!=b)

a = 20 
b = 20 
print(a!=b)

#Is a grather than b

a = 20 
b = 20 
print(a>b)

a = 20 
b = 20 
print(a<b)

#Ia a grather than or equan b

a = 20 
b = 20 
print(a>=b)

a = 20 
b = 20 
print(a<=b)


#Assignment Operators

num = 10

num += 6
print(num)   #num = num + 6 = 10+6 = 16


num = 10
num -= 8 
print(num)   #num = num - 8 = 10-8 = 2

num = 10
num *= 3 
print(num)   #num = num * 3 = 10*3 = 30

num = 10
num /= 6 
print(num)   #num = num / 6 = 10/6 = 1.6666667

num = 10
num %= 4 
print(num)   #num = num % 4 = 10%4 = 2

num = 10
num **= 4 
print(num)   #num = num ** 4 = 10**4 = 10000

# Logical Operations
#not
a = 2
b = 4
print(a>b)
print(not(a>b))

a = 9 
b = 9
print(a==b)
print(not(a==b))

#and : To print True , every conditions must be True

a = True
b = True
print(a and b)

a = True
b = False
print(a and b)

a = False
b = False
print(a and b)

#or : To print true one of the condetions have to be True

a = True
b = True
print(a or b)

a = True
b = False
print(a or b)

a = False
b = False
print(a or b)



#type convarsion : Integer to float , Python does itself

a = 3
b = 2.64
print(a + b)

#type casting // a = data type("XXXX")

# a = "reduan" 
# b = 3
# print(a+b)
# invalid

# a = "2" 
# b = 3
# # print(a+b)
# # invalid
# print(type(a))

a = int("2")
b = 3
print(a+b)

a = 3.9955
b = float("6")
print(a + b)


# take input from the users
#Result for input( ) is always a string
# int(input(X)) #input is intiger value
# float(input(X))  #input is afloat value

#take details and welcome user

name = input("Enter your name :")
age = int(input("Enter your age :"))
date_of_birth = input("Enter your date of birth :")

print("Hello! Mr.", name )
print("Your age is ", age )
print("Your date of birth is ", date_of_birth )