                                 #Function and Recursion
                               #block of statemnts that's Perfrom a specific tasks

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""""""""""""""""""""""""""""""""""""##

#function defenation

def cal_sum(a,b): #Parameters
    sum = a+b
    print(sum)
    return

sum = cal_sum(2231,3345)#function call;arguments
print(sum)#none

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##


#001

#avg of 3 numbers 
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

cal_avg(22,5,8)

#002

#mulp 2 numbers:
def cal_mulp(a,b):
    mulp =a*b
    print(mulp)
    return mulp

cal_mulp(3,7)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#mulp 2 numbers:

def cal_mulp(a=1,b=2): #only first defult argument
    mulp =a*b
    print(mulp)
    return mulp

cal_mulp()
                      
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##


#pratice program
#001
cities = ["nagpur","sadar","raj nagar","rajisthan"]
name=["rishabh","raj","pratik","sagar","kishan"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(name)

#002

cities = ["nagpur","sadar","raj nagar","rajisthan"]
name=["rishabh","raj","pratik","sagar","kishan"]

def print_len(list):
    print_len(list)

print_len(cities)
print_len(name)

#002
#for finding a factorial:

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact

cal_fact(7)
    

#003
#usd conveters in rupes:

def converter(usd_val):
    inr_val = usd_val * 93.83
    print(usd_val,"USD=", inr_val,"INR")

converter(810)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#004 h.w

def num_val(fun):
    if fun %2 == 0:
        print("even")
    else:
        print("odd")

num_val(8)

num_val(4)
num_val(7)
num_val(32)
num_val(81)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##
    


##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""""""""""""""""""""""""##


                                      #Recursion
                           #when a function calls itself repeatedly


def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)

show(7)
print("end")

def fact(n):
    if (n==1 or n == 0):
        return 1
    return fact(n-1)*n
print(fact(4))

def cal_sum(n):
    if (n==0):
        return 0
    return cal_sum(n-1)+n

zz=cal_sum(5)
print(zz)

def print_list(list , idx =0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","banana","apple","litchi"]

print_list(fruits)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##


