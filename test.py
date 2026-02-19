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

# def Reverse_Number(numb):
#   reverse_n = 0
#   while numb > 0:
#     numb % numb 


# Prime Number Check
# Multiplication Table Generator
# Pattern Printing
# Inverted Pattern
# Number Pyramid
# Strong number wo hota hai jisme digits ke factorial ka sum original number ke equal ho.