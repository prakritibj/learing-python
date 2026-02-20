print("hello world")
# print(site_name)
site_name = 'programiz.pro'
# print(site_name)

# # list literal
# fruits = ["apple", "mango", "orange"] 
# print(fruits)

# # # tuple literal
# # numbers = (1, 2, 3) 
# # print(numbers)

# # # dictionary literal
# # alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
# # print(alphabets)

# # # set literal
# # vowels = {'a', 'e', 'i' , 'o', 'u'} 
# # print(vowels)


# num_string = "13"
# num_integer = 23

# print("Data type of num_string before Type Casting:",type(num_string))

# # explicit type conversion
# num_string = int(num_string)

# print("Data type of num_string after Type Casting:",type(num_string))

# num_sum = num_integer + num_string

# print("Sum:",num_sum)
# print("Data type of num_sum:",type(num_sum))

# number = -10.6

# name = "Programiz"

# # print literals     
# print(5)

# # print variables
# print(number)
# print(name)

# using input() to take user input

# num = int(input('Enter a number: '))

# print('You Entered:', num)

# print('Data type of num:', type(int(num)))

# ============= if else prob================
# num = int(input("Enter a num : "))

# if num > 90:
#     print("Grade A")
# elif num > 75:
#      print("Grade B")
# elif num > 65:
#      print("Grade C") 
# else :
#      print("Grade D")
# ============================= function====================
# def pass_fail(score):
#    if score >= 50:
#      print("passed")
#    else : 
#       print("failed")
   
# pass_fail(60)

# -------------------- for loop
# languages = ['Swift', 'Python', 'Go']
# languages = [1,2,3,4]
# languages = 'Swift'

# access elements of the list one by one
# for abs in languages:
#     print(abs)

# range i s funtion that gives sequense numbers
# for i in range(0, 8):
#     print(i)

# -------------continue break statements

languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'mode':
        break
    print(lang)

languages = ['Swift', 'Python', 'Go', 'C++',"mode" ]

for lang in languages:
    if lang == 'Swift':
        continue
    print(lang)

# nested loop 
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    
    print("-----")
# iterate from i = 0 to 3
# sirf loop chalana hai na hume isliy _
for _ in range(0, 4):
    print('Hi')

# function factorial
def factorial(n):
 result = 1
 for i in range(1 , n+1):
      result = result*i
 return result

print(factorial(5))

number = 1

while number <= 3:
    print(number)
    number = number + 1
