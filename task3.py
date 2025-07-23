'''Three parts 
input from user variable declare 
formula implementations k inka krna kia hai  #
 in sb ko print krwayn gy'''

# 4 numbers ko ly lty hn jinki input leni hai..
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
num4 = float(input("Enter 4th number: "))

# All number ko jma krna hai yahan + = (sum)
sum_result = num1 + num2 + num3 + num4  
# All numbers ko Tafreeq krny ka formula  - = difference (diff)
diff_result = num1 - num2 - num3 - num4
# Zarb  nikalna * = product (prod)
prod_result = num1 * num2 * num3 * num4
# Division nikalna / = division (div)
div_result = num1 / num2 / num3 / num4

 # Result print karna
print("your Sum is :", sum_result)
print("your Difference is :", diff_result)
print("your Product is :", prod_result)
print("your Division is :", div_result)
print("Thank You So Much ")

#  Kya mere answers theek hain?
kia_answer_mery_thk_hn = input("Kya mere answers theek hain? (y/N): ")

# If  'yes' print  thank you so much!
if kia_answer_mery_thk_hn == "y":
    print("Thank you so much!")

# Agar jawab 'no' ho to himmat dena
elif kia_answer_mery_thk_hn == "n":
    print("Next time I will try my best.")

# Agar user kuch aur likhe to error message dena
else:
 print("Please type only according to the spelling 'y or 'n1")
