# a,b=3,2
# print(a+b)
# numbers: list[int] =[1,2,3,4,5,]
# print(sum(numbers,start=100) )
# lists: list=[[1,2],['a','b']]
# print(sum(lists, start=[]))

# def my_generator():
#     for i in range(500):
#         yield i 
# #print(next(my_generator()))   

# for j in my_generator():
#     print(j)

# def avg (a= int(input("Enter the Number")),b=int(input("Enter the Number")),c=int(input("Enter the Number"))):
#    # average = (a+b+c)/3
#     return (a+b+c)/3

# print(avg())
# def Checker(num = int(input("Enter the Number: "))):
#     return "Even" if num%2==0 else "odd"
    # if (num%2 == 0 ):
    #     print(num,"is Even")
    # else:
    #     print(num,"is Odd")
        
        
# print(Checker())


# n = int(input("Enter the number:"))
# def num(n):
#     if (n==0):
#         return 0
#     #print(n)
#     a=num(n-1) +n
#     return a
# print(num(n))


#Check the number is Prime or not
num = int(input("Enter the Number"))
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")    