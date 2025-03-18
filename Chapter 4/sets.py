sets = {1,2,3,4,2,2,"Utkarsh","Thakur","Utkarsh"} #Set ignores the repeated value...
sets.add("Age : 18")
print (sets)
print (type(sets))
print (len(sets)) #Totla number of items

#Syntax of Empty set in Python
collection = set() #Empty Set

print (type(collection))

collection.add("First_Name : Utkarsh") #Adds An Element in Sets
collection.add("Last_Name : Thakur")
collection.add ("Age : 18")
collection.add (90152978)
collection.remove(90152978) #Removes The Element From The Set


print(collection.union(sets)) #Combines Both Set Values And Returns New
print(collection.intersection(sets)) #Combines The Common Values And Return New.

print(len(collection))

print (collection) 
print (collection.pop()) #Randomly Removes The Values...
print(collection.clear()) #Empties the Set


set1 = {1,2,3}
set2 = {3,4,5}

print (set1.union(set2))
print (set1.intersection(set2))