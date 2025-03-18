#Store Word Meaning IN Python Dictionary

dictionary = {}

dictionary ["table"] = {"a piece of furniture",
                        "list of facts & Figures"}
dictionary ["cat"] = "a small animal"
print (dictionary)
print(type(dictionary))

#Alternative
dict = {
    "table" : ("a piece of furniture", "list of facts & Figures"),
    "cat" : "a small animal ",
}
print (dict)


#You are given a list of subjects for Students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
sets = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print ("The no. of required classroom needed by all students are :", len(sets))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an Empty dictionary & add one by one. Use subject name as key & marks as value.

empty = {}

a = int(input("Enter the marks of Java :"))
empty.update({"Java" : a})
b = int(input("Enter the marks of Software Engg. :"))
empty.update({"Software Engg." :b})
c = int(input("Enter the marks of Cyber Ethics :"))
empty.update({"Cyber Ethics" : c})

print(empty)


#Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in datatypes)

collection = {
   ( "float", 9.0),
   ( "int",9),
}
print (collection)

#Alternative

collect = {
    9.0,
    "9"
}
print (collect)