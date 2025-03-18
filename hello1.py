# #Take a string input and replace all 'e' with 'k' if the string is longer than 5 characters otherwise print it unchanged.
# str = input("Enter the String: ")
# if len(str)<=5>0:
#     print(str.replace('e','k'))
    
# else:
#     print("unchanged") 

#Take a string from user and use for loop to print each character until a vowel is encountered, Exit program if vowel is "found", if not then print "vowel not found"

str= input("Enter the string: ")
vowel = "aeiou"

for letter in str:
    if letter in vowel:
        print("Vowel is Found", letter)
        break
else:
        print("Vowel Not Found")