  
              #
              # 1 DATA TYPES AND VABRIABLE
               #
####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##########"
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##
#arithmatic operator
a = 5 
b = 2    

print(a + b )
print(a-b)
print(a*b)
print(a/b)
print(a%b)#remainder
print(a**b)#a^b

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#relational operation
a = 50 
b = 20

print(a==b)#False
print(a!=b)#True
print(a>b)#True
print(a<=b)#False
print(a<b)#False

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#assignment operators
num = 10 
num = num +10
num +=10
num -=10
num /= 5
num %= 5
num **=5
print("num:",num)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#logical operators

a = 50 
b = 20
print(not False)
print(not True)
print(not (a >b))

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#and or OR not operators

val1 = True
val2 = False

print("ans operator:", val1 and val2)
print("AND operators:", val1 and val2)
print("OR operators:", val1 or val2)

print("OR operators:",(a==b)or (a>b))#TRUE

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#TYPE COVERTION

#convestion in which atuo converted
a = 2 #if the "2" its stirng that not copatable to add thus we put he data type to convert it
b = 4.25

sum = a + b
print(sum)

#type casting in we do muanal converted
a= float("2")
b = 4.25
sum = a + b
print(type(a))
print(sum)

a = 3.45
a = str(a)
print(type(a))

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#input in pyhton 
int("5")
val = str(input("enter your value:",))
print(type(val),val)


int("5")
val = float(input("enter your value:",))
print(type(val),val)

name = input("enter you name:")
age = int(input("enter your age:"))
marks= float(input("enter you marks:"))

print("welcome",name)
print("age =", age)
print("marks =",marks)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#pratices quation
#001
a = int(input("enter your number:"))
b = int(input("enter your number:"))
sum = a + b

print("sum:",sum)

#002

side = float(input("enter square side:"))
print("area =", side *side)

#003
a = float(input("enter first:"))
b = float(input("enter second:"))
print("avg =", (a+b/2))

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""END""""""""""""""""""""""""""""""""""""""""""""""'##