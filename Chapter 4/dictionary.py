'''dict = {
    "name" : "Python",
    "age" : 18,
    "Mobile_no" : 90152978,
    "Branch" : "Computer Engg."
}
dict ["surname"] = "Thakur"   #This will also include in Dictionary
dict ["name"] = "Utkarsh Thakur"
print(dict ["name"])   #This will print the value assigned to key in Dictionary
print(dict)
'''
#Adding Values in null Dictionary
"""
null_Dict = {}

null_Dict ["name"] = "Utkarsh Thakur"

print(null_Dict)
"""

#Nested Dictionary

dict = {
    "Name" : "Utkarsh Thakur",
    "Subject" : {
        "Java" : 54,
        "Cyber Law" : 42,
        "Software Engg." : 44
    },
    "CGPA" : 8.62,
}
'''
print (dict)
print(dict ['Subject'])  
print(dict ["CGPA"])
print (dict ["Subject"]["Java"])


#Dictionary Methods
print(dict.keys()) #Returns All Keys

#Typecasting the Dictionary in List
print(list(dict.keys()))
print (len(dict)) #Print the Length of Dictionary
print (len(list(dict.keys())))

print(dict.values()) #Returns all Values, It can also be Converted into List 
'''

pair = list(dict.items()) #Returns all (key,val) pair as tuples
print(pair[0])

print(dict.get("CGPA")) #Returns the key according to value
print(dict["Name"])
print(dict.get("Name"))
#These both Methods are correct but in first mehtod if we enter a wrong key then it will show error but in second method if we enter a wrong key then it will display none...
print(dict.get("My_Name"))

dict.update({"City" : "Sundernagar"}) #Inserts the Specified items to the Dictionary
print(dict)

new_dict = {
    "College" : "Goverment Polytechnic College Sundernagar",
}

dict.update(new_dict)
print(dict)
