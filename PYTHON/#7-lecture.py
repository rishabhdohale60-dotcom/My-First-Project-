# File,\n handaling

# Type of file 
# 1.text files : txt,docx,log ,etc...........
# 2.binary files: Mp4,Mov,Png,Jpeg,etc..........

# open ,Read & close file 

# r = read 
# w = write
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""####"
# f= open ("file_name","mode")

# f = open("demo.txt", "w")
# f.write("rishabh is boy,\n lan, lan ,lan lan ,4344")
# f.close()


# f = open ("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


#its not workssss
# f = open("simple.txt","a+")
# f.write("meh rishabh \n how are you deero")
# # print(f.read())
# f.close()

##""""""""""""""""""""""""""""""""""""""""""""""""""""""####"

# withSyntax

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

##"""""""""""""""""""""""""""""""""""""""""""""""""""""####"

#deletings a file

# os modual
# import os 
# os.remove("simple.txt")   #its worksssssssss

##""""""""""""""""""""""""""""""""""""""""""""""""""""####"

#practice program

#001
# with open("practice.txt","w") as f:
#     f.write("hi everyone\n we are learning file I/O \n")
#     f.write("using Java \n I like Programming in Java")

##""""""""""""""""""""""""""""""""""""""""""""""""""""####"

#002
with open("practice.txt","r") as f:
    data =f.read()
    
new_data = data.replace("Java","python") #Java!=java
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

##""""""""""""""""""""""""""""""""""""""""""""""""""""####"

#003

# word = "xlearnig"
# with open("practice.txt","r") as f:
#     f.read()
#     if(data.find(word)!=-1):
#         print("Found It")
#     else:
#         print("Not Found")

##""""""""""""""""""""""""""""""""""""""""""""""""""""####
#003
# ''''''''''''''''''''''''''OR''''''''''''''''''''''#

# def check_for_word():
    
#         word = "learning"
#         with open("practice.txt","r") as f:
#             f.read()
#         if(word in data):
#             print("Found It")
#         else:
#             print("Not Found")

# check_for_word()

##""""""""""""""""""""""""""""""""""""""""""""""""""""####

# def checl_for_line():
#      word="python"
#      data=True
#      line_no =1
#      with open("practice.txt","r") as f :
#           while data:
#                data = f.readline()
#                if(word in data):
#                     print(line_no)
#                     return
#                line_no+=1
# checl_for_line()

##""""""""""""""""""""""""""""""""""""""""""""""""""""####


# with open("practice.txt","w"):
#      data=f.write("1,45,35,67,39,87,97")
#      print(data)

with open("practice.txt","r")as f:
     data = f.read()
     print(data)

     num=""
     for i in range(len(data)):
          if (data[i]) ==",":
               print(int(num))
               num =""
          else:
               num+=data[i]

##""""""""""""""""""""""""""""""""""""""""""""""""""""####


count = 0 
with open("practice.txt","r") as f :
     data= f.read()

     num = data.split(",")
     for val in num :
          if (int(val) %2==0):
               count+=1

print(count)

##"""""""""""""""""""""""""""""""""END"""""""""""""""""""####
