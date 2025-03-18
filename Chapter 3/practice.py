#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
'''
movie1 = input("Enter the Name of your favorite movie")
movie2 = input("Enter The Name of your favorite movie")
movie3 = input("Enter the name your favorite movie")
favorite_movies = []
favorite_movies.append(movie1)
favorite_movies.append(movie2)
favorite_movies.append(movie3)
print (favorite_movies)'''

#Alternative
'''
movies = []
movies.append(input("Enter1st movie "))
movies.append(input("Enter 2nd movie "))
movies.append(input("Enter the 3rd movie "))

print(movies)
'''
#Both Are same and will execute correctly 

#WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
'''
palindrome_list = [1,'abc','abc',1]
a= palindrome_list.copy()
print(a)
a.reverse()
print(a)

if(a== palindrome_list):
    print("Palindrome")
else: 
    print("NOT Palindrome")
'''

#WAP to count the number of students with the "A" grade in the following tuple.
'''tup = ("C","D","A","A","B","B","A",)
print(tup.count("A"))
'''
#Stores the above values in a list & sort them from "A" to "D"

list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)