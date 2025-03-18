'''
output = open('hello.c','r')

data= output.readline()
print(data)

data1= output.readline()
print(data1)
output.close()
'''
'''
output = open('hello.c','w')
data = output.write("Hello World ")
data = output.write(" \n My name is utkarsh thakur")

output1 = open('hello.c','a')
data1= output.write("\n Glad to know about you")

#print(data)
print(type(data))
output.close()
'''
'''
a = open('sample.py','a')#This Will Create a file in your folder
a.close()

a = open('sample.py','w')
data = a.write("a,b=3,2")
a = open('sample.py','a')
data = a.write("\nprint(a+b)")
a.close()
'''
'''
#Opening a file with 'with' Syntax
with open('hello.c','r')as f:
    data = f.read()
    print(data)
    '''

#Create a new file "practice.txt" using Python. Add the data in it:

f = open('practice.txt','w')
data = f.write("Hello Everyone")

f.close()
#f= open('practice.txt','w')

with open('practice.txt','a') as u:
    data = u.write("\nMy Name is Utkarsh Thakur \n we are learning File I/O \n using Java. \n I like programming in Java")
    print(data)


    #TO remove the file from we need to import module

   # import os 
    #os.remove('ab.py')

    #Write a function that replaces all occurences of "Java" with "Python" in above files.
with open('practice.txt','r') as u:
    data = u.read()
    print(data)
    new_data = data.replace("Java","Python")
    print(new_data)


with open('practice.txt','w') as y:
    y.write(new_data)
    print(new_data)

#Search if the word "learning" exists in the file or not.
with open('practice.txt','r') as y:
   data= y.read()
   search="learning"
   if(search in data):
       print("Found")
   else:
       print("Not Found")
print(data)


#Write a function to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
def find_line():
    with open('practice.txt','r') as y:
     line_no = 1
     data= y.readline()
     search="learning"
     while True:
        data= y.readline()
        if (search in data):
           print(line_no)
           line_no +=1

print(find_line())

