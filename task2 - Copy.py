# task2 ..(i)
# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# subject Marks input 
english_marks = int(input("Enter English marks: "))
math_marks = int(input("Enter Math marks: "))
science_marks = int(input("Enter Science marks: "))
# Total marks nikalna (Arithmetic operator)
total = english_marks + math_marks + science_marks
# Bonus marks add karna (Assignment operator)
total += 5  # Same as total = total + 5
# Check pass/fail (Comparison + Logical operators)
is_pass = (english_marks >= 33) and (math_marks >= 33) and (science_marks >= 33)
# using if else
if (english_marks>=33) and (math_marks>=33) and (science_marks>=33):
    print ("you are pass")
else:
    print("you are fail")
#: Output dikhana
print("--- Student Result ---")
print("Name:", name)
print("Age:", age)
print("Total Marks (with bonus):", total)
print("Pass Status:", is_pass)'''

'''# task2 ..(ii)
# Step 1: User se do numbers 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
# Step 2: Basic operations karna
add = number_1 + number_2
sub = number_1 - number_2
mul = number_1 * number_2
prod = number_1 * number_2
div = number_1 / number_2  # division hamesha float deta hai
div_floor = number_1 // number_2 #is mn without flotr deta hai 
expo= number_1 ** number_2
# Step 3: Assignment operator (update numer_1 number)
number_1 += number_2  # same as number1 = number1 + number2
# Step 4: Comparison operator se check karna
is_greater = number_1 > number_2  # True ya False dega
# Step 5: Final output dikhana
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division:", div)
print("Division floor: ", div_floor)
print("exponentional value : ", expo)
print("Updated first number: ", number_1)
print("Is first number > second number? ", is_greater)'''
'''# task2 ..(iii)
name = input("enter your name: ")
age = int(input("enter your age: "))
# Check if age is greater than or equal to 18.
# If yes, print "You are eligible for ID card."
if age >= 18:
    print("You are eligible for ID card.")
elif age < 18 > 10 :
    print ("You are a teenager.")
else:
    print ("You are a child.")'''

