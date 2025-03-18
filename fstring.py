letter = "My name is {} and I am pursuing {}"
name = "Utkarsh Thakur"
deptt = "Computer Engg."
print(letter.format(name, deptt))

#Or we can say that we can give index from which we can specify which arguement will be executed first

letter1 = "I am {1}, I love {0} and per semester fee {2}"
age = 18
language = "Python"
sem_fee = 1400
print(letter1.format(language, age, sem_fee))

#:.2f only execute the decimal value 
x="1 Dollar is {rs:.2f} "
print(x.format(rs = 42.004), "Rupees")

#OR we can write this using f strings

y= 90.345
print(f"1 Dollar={y:.2f} Rupees")

#To print multiplication of any number as a string
print(f"{2*30}")

#Double curly brackets {{name}} like this are used to print to get output like {name}






















# name = input("Enter Your Name ")
# age =  int(input("Enter Your Age "))

# if name==name and age ==age:
#     print( f"Your name is {name} and Your age is {age} Right??")
# user = input("Y/N: ")
# if user =='y':
#         print("Congratualtions...")
# else:
#         print("Error Found")
        

