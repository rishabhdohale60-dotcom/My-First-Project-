                                #loop in python/iteration 

                                        # while True:
#   print("hello world")
    #infinty loop

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""""""""""""""""""""""""""""""""""""##

count=1
while count <=5 :
    print("right",count)
    count+=1

i = 1 
while i <= 6:
    print("i king",i)
    i +=1
print("loop end")

i = 5 
while i >= 1:
    print("i king",i)

    i -=1
print("loop end")


i = 5 
while i < 6 :
    print("i king",i)
    i -=1
print("loop end")  

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##


#program [pratices]

##code1
i =1
while i <= 100 :#stoping comdition
    print(i)
    i+=1

i =100
while i >= 1 :#stoping comdition
    print(i)
    i-=1

# code2
                      # for printing a multiplcation table

i =1
while i<=10:
    print(3*i)
    i+=1
                      

#code3

num = [1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100]

z = 0
while z < len(num):
    print(num[z])
    z += 1


##code4
num = [1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100]

x= 49
i=0
while i < len(num):
     if(num[i]==x):
        print("FOUND AT Z",i)
     else:
         print("JUST FIND")
     i +=1

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""#

#appelid the break key-word
'''   
i = 0
while i <=5:
    if(i==3):
        i+=1
        break
    print(i)
    i +=1


# continue

i = 0
while i <=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i +=1



i = 0
while i <10 :
    if(i%2!=0):
        i+=1
        continue   #skip
    print(i)
    i +=1 '''

# """"""""""""""""""""""""""""""""""""""""""""""""""#

#using for loop
'''
num =[1,2,3,4,5,6,7,8,9]
for val in num:
    print(val)

tup =(2,4,5,6,2,5,6,6,3)
for val in tup:
    print(val)


str = "rishabh"
for el in str:
    print(el)
else:
    print("end")


# """"""""""""""""""""""""""""""""""""""""""""""""""#

num = [1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100]
for el in num:
    print(el)


nums = (1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100)
x = 36
c = 0
for eel in nums:
    if (eel==x):
        print("found it",c)
        break
    c+=1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 72, 81, 100)
x = 36
c = 0
for eel in nums:
    if (eel==x):
        print("found it",c)
        pass
    c+=1


# """"""""""""""""""""""""""""""""""""""""""""""""""#

##Range()
for el in range(4):
    print(el)

for el in range(4):
    pass
    print(el)    


seq = range(20)###stoping condition
for ell in seq:
    print(ell)

for xe in range(1,7,3):#its has start,stop,step
    print(xe)

for xe in range(2,100,5):#its has start,stop,step
    print(xe)   
'''

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#pracrice program

for i in range(1,101):
    print(i)

for z in range(101,0,-1):
    print(z)


#"""""""""""printing the mulitiplecaiton table###

n = int(input("enter your number:",))
for i in range(1,11):
    print(n*i)

#001
n =5
sum = 0
for i in range(1,n+1):
    sum+=i
    i +=1
print("total sum=",sum)


#002
n = 7
sum=0
i =1
while i<=n:
    sum +=i
    i +=1

print("total sum:",sum)


# 003
#""" for finding factoral"

n = 5
fact = 1
i =1
while i<=n:
    fact *=i
    i +=1

print("fact=",fact)


n = 5
fact = 1
i =1
for i in range(1,n+1):
    
    fact *=i
    i +=1

print("fact=",fact)


##""""""""""""""""""""""""""""""""ENDD""""""""""""""""""""""""""""""""""""""""""""##
