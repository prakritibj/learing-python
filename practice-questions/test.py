# WAF even odd
def check_even_odd(num):
  if num % 2 == 0 :
   print("even")
  else :
   print("odd")
check_even_odd(2)

# WAF find bigger 
def find_max(a ,b):
   if a > b :
     return a
   else:
     return b

print(find_max(30,20))

# Operator ho sakta hai: +, -, *, / otherwise return "Invalid Operation"

def calculater(a, b ,oprater):
  if oprater == "+":
    return a+b
  elif  oprater == "-":
     return a-b
  elif oprater == "*":
     return a*b
  elif  oprater == "/":
       if b != 0:
        return a / b
       else :
         return "divied by zero not allowed"

  else: 
    return "Invalid Operation"
  
  
print(calculater(10,0,"/"))

# --------------------------Level 2 – Loop + Function Combo---------------------

# Sum of First N Numbers
def sum_number(a):
  total = 0
  for i in range(1,a+1):
     total += i
  return total

print(sum_number(6))

# Count Vowels in String
def count_vowels(text):
   count = 0
   vovel = "aeiouAEIOU"
   for charater in text:
      if charater in vovel:
          count += 1
  
   return count
     
print(count_vowels("hariom"))
# ========================================================
# Reverse a Number
def reverse_number(numb):
    reversed_num = 0
    
    while numb > 0:
        digit = numb % 10          # last digit nikalna
        reversed_num = reversed_num * 10 + digit
        numb = numb // 10          # last digit remove karna
    
    return reversed_num
print(reverse_number(123))

# Prime Number Check

# Multiplication Table Generator
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)

# Pattern Printing
def pattern(n):
    for i in range(1, n+1):
        print( "*" * i )

pattern(6)

# Inverted Pattern
def Inverted_pattern(n):
    for i in range(n, 0 ,-1 ):
        print( "*" * i )

Inverted_pattern(6)
# Number Pyramid
def pattern(n):
       for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

pattern(6)

# Strong number wo hota hai jisme digits ke factorial ka sum original number ke equal ho.