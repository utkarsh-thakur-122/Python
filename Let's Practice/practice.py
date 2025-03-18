#Program to determine the data type of a given variable
'''a = 2
b = "Utkarsh Thakur"
print (type(a))
print (type(b))
'''

#Convert a given integer to a float, and vice versa
'''a = 2
b = float(a)
print (b) 
'''

#Convert a string to an integer 
'''a = "50"
b = int (a)
print (b)
print (type(a))
print (type(b))
''' 

#Calculate the area and the perimeter of Rectangle
'''a = int(input("Enter the length of Rectangle "))
b = int(input("Enter the Breadth of Rectangle "))
area = a*b
perimeter = 2*(a+b)
print(area)
print (perimeter)
'''

#Implement a Simple Calculator
'''
num1 = 5
num2 = 2
add = num1+num2
product = num1*num2
sub = num1-num2
quotient = num1/num2
remainder = num1 % num2

print ("Addtion: ",add)
print ("Multiplication", product)
print ("Subtraction", sub)
print ("Quotient", quotient)
print ("Remainder",remainder)
'''

#Write a program to check if a number is a even or odd
'''
a = int(input("Enter the number: "))

if (a%2 ==0 ):
    print("Even Number")
else:
    print("Odd Number")
'''

#Print the numbers from 1 to 10
'''
a =1
while a<=10:
    print(a)
    a+=1
    '''

#Create a list pf a fruits and print them.
'''
list = ["Apple", "Banana", "Mango", "Grapes", "Apple"]
list.insert(0,"Mango")
list.append("Grapes")
print(list)
'''

#Create a tuple of colors and print it.\
'''
colour = ("Red", "Green", "Yellow", "Black")
print(colour)
print(type(colour))'''

#Create a Dictionary of Student names and their scores.
'''dict = {"Utkarsh" : 56,
        "Rishav" :56,
        "Virender" : 54,}
print(dict)
'''

#use of continue statement
'''i = 1
while i<=5:
    if(i==3):
        i+=1
        continue
    
    print(i)
    i+=1
'''

#Use Continue Statement to Print the odd numbers upto 10.
i = 1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    
    print(i)
    i+=1

