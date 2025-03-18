#while loop

'''count = 1
while count <=5 :
    print("Hello World", count)
    count = count+1  #Or count+=1
'''
#To print numbers using while loop
'''
i = 1
while i<=5:
    print(i)
    i +=1
'''



#Let's Practice

#Print numbers from 1 to 100.
'''count = 1
while count<=100:
    print(count)
    count += 1
print ("Success")
'''

#Print numbers from 100 to 1
'''i = 100
while i>=1:
    print (i)
    i-=1
print ("Success")
'''
#Print the Multiplication table of a number n
'''n = int(input("Enter the no."))
i = 1
while i<=10:
    print(n,"X",i,"=",n*i)
    i= i+1
  '''

#Print the elements of the following list using a loop:
'''
list = [1,4,9,16,25,36,49,64,81,100]
index= 0
while index < len(list):
    print (list[index])
    index +=1
'''
#Search for the number x in the tuple using loop:
'''tup = (1,4,9,16,25,36,49,64,81,100)
x = 49
index = 0
while index < len(tup):
    if (tup[index]== x):
        print ("Found at Index :", index, tup[index])
        break
    print (index,tup[index])
    index += 1
'''

#Print odd no. using Continue
'''i =1
while i<=10:
    if(i%2 == 0 ):
        i+=1
        continue
    print(i)
    i+=1
'''

#Using for loop to print letter of names
'''
String = "Utkarsh Thakur"
for i in String:
    if (i=="a"):
        print("Found at index", String.index("a"))

    print(i)
else:
    print("END")
'''

#Print the elements of the list using a loop: (Also known as linear search)
'''
list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    if(i == 36):
        print(i,"Found at index",list.index(36))
    print(i)
else:
    print("Executed Successfully")
'''

#To Print Odd numbers by user input using for loop:
'''num = int(input("Enter the number from where you want to start "))
end = int(input("Enter the number at which you want to end"))
for i in range(num,end):
    if(i%2 != 0):
     print(i)
   '''

# To print Even numbers by user input using for loop:
'''
num = int(input("Enter the number from where you want to start "))
end = int(input("Enter the number at which you want to end"))
for i in range(num,end,2):
   
     print(i)
'''

#Print numbers from 1 to 100
#for i in range(0,101):
 #  print(i)
   

 #Print numbers from 100 to 1
'''
for i in range(100,0,-1):
    print(i)
'''

#Print the multiplication table of a number n 
'''
a = int(input("Enter the input from the user: "))

for i in range(1,11):
    print(a,"X",i,"=",a*i)
'''
#Pass Statement 
'''
for i in range(5):
    pass
print("Do Some Useful Work")'''

#WAP to find the sum of first 5 natural numbers using for loop
'''
sum =0
for i in range(1,6):
    
    sum += i
    print("Sum is", sum)
'''
#WAP to find the factorial of first n natural number using for loop
n = int(input("Enter the number "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial", fact)