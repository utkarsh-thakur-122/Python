'''
def fun(n):
    if (n==6):
        return
    print(n)
    fun(n+1)  
fun(1)
'''

#Find the Factorial using recursive Method
'''
n = int(input("Enter the number you want to check the Factorial: "))
def fun(n):
    if (n==1 or n==0):
        return 1
    a = fun(n-1) 
    fact = a*n  #If we want, We can directly multiply the n in variable 'a' i.e. a= fun(n-1)*n
    return fact
print(fun(n))
'''

#Write a recursive function to calculate the sum of list n natural numbers
'''
n = int(input("Enter the number:"))
def num(n):
    if (n==0):
        return 0
    #print(n)
    a=num(n-1) +n
    return a
print(num(n))
    '''

#Write a recursive function to print all elements in a list.(Hint: use list & index as parameters.)
'''
def print_list(list = ['a','b','c','d'], idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1) 
print_list()
'''


def fun(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    fun(list, index+1)

fun(list = ['Sundernagar','Mandi','Solan','Shimla','Jogindernagar'])
