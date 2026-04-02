# #python is a interpreted programming language 
# #python use both compiller and interpreter

# math = 15 
# name = "sahil"
# pi = 3.14
# result = True

# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# #python interpreter at runtime decides the value



# math = 15 
# name = "sahil"
# pi = 3.14
# result = True
# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# # address show 

# math = 50
# chem = 50

# print(id(math))
# print(id(chem))
# # here same memory is allocated for math and chem



# # type casting 
# #conversion value from one datatypoe to another datattype is called as type casting

# print(2+2)
# print("2"+"2")
# val1 = int(input("Enter a value of val1: "))
# val2 = int(input("Enter a value of val2: "))
# print(val1 + val2)

# # input function by default accept only string  value



# print(int(3.14))
# #print(int(10=5j))
# print(int(True)) #1
# print(int(False)) #=0
# #print(int("4.34"))
# print(int("4"))


# # float used to convert
# print(float(3))
# # print(float(40+4j))
# print(float(True)) #1.0
# print(float(False)) #0.0
# print(float(3.14))
# print(float("4"))
# # print(float("name"))

# print(complex(3))
# print(complex(40 + 4j))
# print(complex(True))    # (1+0j)
# print(complex(False))   # 0j
# print(complex(3.14))
# print(complex("4"))
# # print(complex("name"))
# # print(complex("name"))  # This will give an error


# print(bool(3))
# print(bool(40 + 4j))
# print(bool(True))
# print(bool(False))
# print(bool(3.14))
# print(bool("4"))
# print(bool("name"))


# val1 = int(input("Enter a number: "))
# val2 = int(input("Enter another number: "))

# temp = val1
# val1 = val2
# val2 = temp
# print("After swapping:")
# print("First number:", val1)    
# print("Second number:", val2)






# val1 = int(input("Enter a number: "))
# val2 = int(input("Enter another number: "))

# val1=val1 + val2
# val2=val1-val2
# val1=val1-val2

# print("After swapping:")
# print("First number:", val1)    
# print("Second number:", val2)







# p1 = int(input("Enter a marks of p1: "))
# p2 = int(input("Enter a marks of p2: "))
# p3 = int(input("Enter a marks of p3: "))
# total = p1 + p2 + p3
# percentage = (total / 300) * 100
# print("Total marks:", total)
# print("Percentage:", percentage)




#  #simple intrest 
# p_amount = int(input("Enter the principal amount: "))
# roi = float(input("Enter the rate of interest (in %): "))
# time = int(input("Enter the time (in years): "))
# si = (p_amount * roi * time) / 100
# print("Simple Interest:", si)  





# # conversion of height to feet and inches
# height_feet= float(input("Enter your height in feet: "))
# height_inch = height_feet * 12
# cm = height_inch * 2.54
# print("Your height in inches:", height_inch)
# print("Your height in cm:", cm)





# num = 123
# a = num % 10
# num = num // 10
# b= num % 10
# c= num // 10
# rev = a*100 + b*10 + c*1
# print("Reverse of the number is:", rev)





# num = 123456

# a = num % 10
# num = num // 10

# b = num % 10
# num = num // 10

# c = num % 10
# num = num // 10

# d = num % 10
# num = num // 10

# e = num % 10
# num = num // 10

# f = num % 10
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print("Reverse of the number is:", rev)









# num = 123456
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reverse of the number is:", rev)





# #when we want to address comparision identity operator is used like is and is not
# a = 10
# b = 10
# print(a is b)  # True
# print(a is not b)  # False




# # membership operator is used to check if a value is present in a sequence (like a list, tuple, or string) 
# # or not. It returns True if the value is found in the sequence, and False otherwise.

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True
# print(6 in my_list)  # False    



# # write a program to identify positive, negative and zero number
# num= int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")    
# else:    print("The number is zero.")





# # find the max number among 5 numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))   
# c=int(input("Enter third number: "))
# d=int(input("Enter fourth number: "))
# e=int(input("Enter fifth number: "))

# if a > b and a > c and a > d and a > e:
#     print("The maximum number is:", a)
# elif b > a and b > c and b > d and b > e:
#     print("The maximum number is:", b)
# elif c > a and c > b and c > d and c > e:
#     print("The maximum number is:", c)
# elif d > a and d > b and d > c and d > e:
#     print("The maximum number is:", d)  
# else:    print("The maximum number is:", e)







# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username ==password:
#     print("Login successful!")
# else:    print("Login failed. Please check your username and password.")






# #write a program to accept phy chem and math marks and calculate total and percentage 
# # if percentage is greater than 60 and gender is equal to male then he eligible for data entry job

# phy = int(input("Enter marks for Physics: "))
# chem = int(input("Enter marks for Chemistry: "))
# math = int(input("Enter marks for Mathematics: "))
# gender = input("Enter your gender (male/female): ")
# total = phy + chem + math
# percentage = (total / 300) * 100
# print("Total marks:", total)
# print("Percentage:", percentage)
# if percentage > 60 and gender == "male":
#     print("You are eligible for the data entry job.")   
# else:    print("You are not eligible for the data entry job.")
    








# # wap a program to accept a value of a b c and find the max value using nested if else

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b:
#     if a > c:
#         print("The maximum number is:", a)
#     else:
#         print("The maximum number is:", c)
# else:   
#     if b > c:
#         print("The maximum number is:", b)
#     else:   print("The maximum number is:", c)     
    
    
    
    
# #write a program to accept all days and print monday to friday as weekday and 
# # saturday and sunday as weekend
    
# day = input("Enter a day of the week: ")
# if day == "SATURDAY" or day == "SUNDAY" or day == "Saturday" or day == "Sunday" or day == "saturday" or day == "sunday":
#     print("It's a weekend.")
# else:
#     print("It's a weekday.")
    
    
    
    
    


# #wap a program to accept one character from keyboard and check it is upper case lower case digit
# # and special symbol so print message with respect to entered value:

# char = ord(input("Enter a character: "))
# if char>=65 and char <=91:
#     print("The character is an uppercase letter.")
# elif char>=97 and char <=122:
#     print("The character is a lowercase letter.")
# elif char>=48 and char <=57:
#     print("The character is a digit.")  
    



# #notes
# amount = int(input("Enter the amount: "))
# print("100 notes =", amount // 100)
# print("50 notes =", (amount % 100) // 50)
# print("20 notes =", ((amount % 100) % 50) // 20)
# print("10 notes =", (((amount % 100) % 50) % 20) // 10)
# print("5 notes =", ((((amount % 100) % 50) % 20) % 10) // 5)

