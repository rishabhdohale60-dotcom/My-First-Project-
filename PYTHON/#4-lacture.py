                                        #dictionary in python 
                                     #store in key.value pairs
                                 #mutable dont allow duplicate value

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

info = {
    "name" : "rishabh",
    "subj" : "icde",
    "age"  : 355,
    55.34  : 56.33

}
print(info)
print(info["subj"])

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#empty dict

null_dict = {}
null_dict["name"]="dohale"
print(null_dict)

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#nested dict

student = {
    "name" : "rishabh dohale",
    "subjects": {
        "phy":43,
        "chem": 34,
        "math": 99

    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#dict method

student = {
    "name" : "rishabh dohale",
    "subjects": {
        "phy":43,
        "chem": 34,
        "math": 99

    }
}
#print(student.keys())

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#type castings

print(list(student.keys()))#return all valuse

print(len(list(student.values())))#return len of valuse

print(list(student.values()))#return all valuse

print(student.items())#return all (key,val) pairs as tuple
new_dict={"name":"raj pande","age": 45 }
student.update(new_dict)

print(len(student))#find the len of strings

print(student.get("name"))#return the valuse that's in keys
print(student["name"])

#student.updated
student = {
    "name" : "rishabh dohale",
    "subjects": {
        "phy":43,
        "chem": 34,
        "math": 99

    }
}
new_dict={"name":"raj pande","age": 45 }
student.update(new_dict)
print(student)


#student.get
student = {
    "name" : "rishabh dohale",
    "subjects": {
        "phy":43,
        "chem": 34,
        "math": 99

    }
}

print(student.get("name"))#return the valuse that's in keys
print(student["name"])

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##



                                                   ##set in pyhton##
                                        #set is the clloection data of the unordered items
                                    # set are muatable  & element are immutable

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##
 
collection = set()
print(type(collection))

#Set method
collection = set()
collection.add(1)#add an element
collection.add(2)
collection.add("reishabh")

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#collection.remove(1)#reomve as element

collection.clear()#for an clear all element
print(collection)

colx = {"hello","rishabh","raj","pratik"}
print(colx.pop())#ramdom val removes


col1 ={3,4,5,6,7,8}
col2 = {1,2,3,4,5}
print(col1.union(col2))


col1 ={3,4,5,6,7,8}
col2 = {1,2,3,4,5}
print(col1.intersection(col2))

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""##

#pratice program 

#001
dict = {
    "cat": "a small animal",
    "table":["a piece of furnitur","list of facts & figures"]
}
print(dict)

#002

set1 = {"python","java","C++","python","javascript","java",
        "python","java","C++","c"}
print(set1)
print(len(set1))

#003
marks={}
x =int(input("enter phy:"))
marks.update({"phy":x})

x =int(input("enter chem:"))
marks.update({"chem":x})

x =int(input("enter maths:"))
marks.update({"maths":x})

print(marks)

#004
val = {9,"9.0"}
print(val)