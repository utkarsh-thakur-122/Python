#Create a function which Calculate Sum of two numbers
'''def CalcSum(a= int(input()),b = int(input())):
    return a+b
sum = CalcSum()
print(sum)
'''

#Create a function which Calculate Average of 3 nunmbers
'''
def avg (a= int(input("Enter the Number")),b=int(input("Enter the Number")),c=int(input("Enter the Number"))):
    average = (a+b+c)/3
    return average

print(avg())

'''
#Alternative to Calculate the Average of 3 numbers
'''
def avg(a,b,c): #a,b,c are the parameters...
    return (a+b+c)/3
average= avg(2,4,6) #Calling the arguments
print(average)
'''

#Write a Function to print the length of a list.(list is the parameter)
'''def animal(list=["Lion","Tiger","Bear"]):
  a=  len(list)
  return a 

print (animal())
'''

#Alternative 
'''
Cities = ["Sundernagar","Sarkaghat","Jogindernagar","Rewalsar"]
District = ["Mandi", "Shimla", "Solan", "Bilaspur","Hamirpur"]

def my_fun(list):       #Here list are the parameters
    return (len(list))

print(my_fun(Cities))      #Cities are the Arguments
print(my_fun(District))     #District are the Arguments

a= my_fun(Cities)
b = my_fun(District)
print (a, end = " $ ")
print (b)
'''

#Write a Function to print the elements of a list in a single line. (list is the parameter)
'''
Cities = ["Sundernagar","Sarkaghat","Jogindernagar","Rewalsar"]
District = ["Mandi", "Shimla", "Solan", "Bilaspur","Hamirpur"]
def my_fun(list1, list2):
    for i in list1, list2:
        print (i,end=", ")
a= my_fun(Cities, District)
print(a)
'''

#Write a Function to find the Factorial of n. (n is the parameter)
'''
def factorial(n):
   
   fact = 1
   for i in range(1,n+1):
    fact *= i
    print("Factorial",fact)
   
print(factorial(5))
'''

#Write a Function to convert USD to INR.
'''
def Converter():
    USD = int(input("Enter the Amount: "))
    INR = 83
    convert = USD*INR
    #print("USD to INR",convert)
    return convert              #Where the value is returned we don't require to print the Function or save the function in another variable. We can Directly Right the Functions.
print("USD to INR: ",Converter())
'''
#Write a Function to check the number entered by user is even or odd
'''
def Checker():
    num = int(input("Enter the Number: "))
    if (num%2 == 0 ):
        print(num,"is Even")
    else:
        print(num,"is Odd")
        
print(Checker())
'''

# def Factorial():
#     num = int(input("Enter the Number: "))
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
        
#     return fact

# print('Factorial of the number: ',Factorial())
# def factorial(n):
   
#    fact = 1
#    for i in range(1,n+1):
#     fact *= i
#     print("Factorial",fact)
   
# factorial(5)

