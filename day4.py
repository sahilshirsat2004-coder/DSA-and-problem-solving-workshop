# print('prashantjha777'.isalnum())  #isalphanumeric
# print('prashant777'.isalpha())   #isalphabetic
# print('777f'.isdigit())
# print('aaesdsfdf'.islower())
# print(''.islower())
# print('prashantj'.isupper())
# print('my name is prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("hello".startswith("He"))
# print("hello".endswith("lo"))

# ----------------------------------------------------------------------------------------------

# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))

# ----------------------------------------------------------------------------------------------

# write a function to check if a key exists in a dictionary using the operator or the get() method

# mydict = {"name": "prashant", "age": 21}
# if "age" in mydict:
#     print("key exists")
# else:
#     print("key does not exist")

# ----------------------------------------------------------------------------------------------

#write a function to count the frequency of elements in a list using a dictionary

# mylist = [1,2,3,4,1,2,3,4,1,3,3,4]
# mydict = {}
# for i in mylist:   
#     if i in mydict:  
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# print(mydict)

# ----------------------------------------------------------------------------------------------

# n1 =  int(input("Enter first value : "))
# n2 =  int(input("Enter second value : "))

# try: 
#     print(n1/n2)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# print("to be continued")

# -----------------------------------------------------------------------------------------------
# try: 
#     n1 =  int(input("Enter first value : "))
#     n2 =  int(input("Enter second value : "))

#     print(n1/n2)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("Enter olny integer value")
# print("to be continued")

# -----------------------------------------------------------------------------------------------

# handle multiple kinds of exception with
# single except block

# try: 
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# --------------------------------------------------------------

# if any third exception is coming at runtime then we can use nested Exception block

# try: 
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# except:
#     print("this  is default part of except block")

# --------------------------------------------------------------

# we can use else block if no error generate it 

# try: 
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# else:
#     print("everything is ok")

# --------------------------------------------------------------

# finally block will be executed always whethr try block generate error or not

# try: 
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ",message)
# finally:
#     print("this will be always executed")
    
# --------------------------------------------------------------

# nested try except block 
# try:
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)       

#  --------------------------------------------------------------

# try:
#     a =  int(input("Enter first value : "))
#     b =  int(input("Enter second value : "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)
# else: 
#     print("there are no error in try block")
# finally:
#     print("i am finally block i will be executed always")    

#  --------------------------------------------------------------

# write an algorithm to find the security key for the data

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]
    
#     j = i + 1
#     while j < len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j += 1
# print(len(newlist))

# --------------------------------------------------------------
    
# find the second largest element

# list = [2,5,4,7,8]
# list.sort()
# print(list)
# print(list[-2])

# --------------------------------------------------------------

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# --------------------------------------------------------------

# username = ""
# password = ""
# while username != "admin" or password != "admin":
#     username = input("enter username: ")
#     password = input("enter password: ")

# --------------------------------------------------------------

#wap to count vowels and consonants in the string
# name = "programming"
# vowels = ['a','e','i','o','u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel += 1
#     else:
#         cons += 1
        
# print("vowels",vowel)
# print("consonants",cons)    
# --------------------------------------------------------------


# # write a function to remove all occurences of a specific elment from a list
# list = [1, 2, 3, 2, 4, 2, 5]
# element = 2

# new_list = []

# for x in list:
#     if x != element:
#         new_list.append(x)

# print(new_list)
# --------------------------------------------------------------


# #write a function to calculate a product of all element in the list using a loop
# lst = [2, 3, 4, 5]

# product = 1

# for x in lst:
#     product *= x

# print(product)


# --------------------------------------------------------------


# f = open("myfile.txt", "w")
# print("File name: ", f.name)
# print("File mode: ", f.mode)
# print("readable: ", f.readable())
# print("writable: ", f.writable())
# print("file.closed: ", f.closed)
# f.close()
# print("file.closed: ", f.closed)

# --------------------------------------------------------------

# # performing write operation
# f = open("myfile.txt","a+",)
# f.write("\n Pune is a smart city")
# f.writelines()
# f.close()
# print("file operation is done")


# #performin write operation

# f = open("myfile.txt", "a")
# f.write("\n Pune is smart city")
# f.close
# print("file operation is done")


# #inserting list
# f = open("myfile.txt", "w")
# mylist = ["Nikhil", "Harshad","Utkarsh","Atharv","Ganesh","Sakharam",77,"Karan",60.52,"Nilesh"]
# f.writelines(myfile)
# f.close
# print("file operation is done")


## --------------------------------------------------------------


# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("nikhil\n")
#     f.write("harshad\n")
#     f.write("utkarsh\n")
#     f.write("atharv\n")
#     f.write("ganesh\n")
#     f.write("sakharam\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)


# # --------------------------------------------------------------
# f1=open("a.png","rb")
# f2=open("a.png","wb")
# data=f1.read()
# f2.write(data)
# print("new img is available here with the name:")


# # --------------------------------------------------------------

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)

# studentid = int(input("enter student id:"))
# rollno = int(input("enter roll no:"))
# name = input("enter your name:")
# mobileno = int(input("enter mobile no:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")

# # --------------------------------------------------------------

# # write a program to take input roll no name mobile no and studenttid  email and marks to tjree sub marks


# import csv
# with open("student.csv", "a", newline="") as f:
#     a = csv.writer(f)

#     studentid = int(input("Enter student id: "))
#     rollno = int(input("Enter roll no: "))
#     name = input("Enter your name: ")
#     mobileno = int(input("Enter mobile no: "))
    
#     p1 = int(input("Enter physics marks: "))
#     p2 = int(input("Enter maths marks: "))
#     p3 = int(input("Enter chemistry marks: "))

#     # Calculate total and percentage
#     total = p1 + p2 + p3
#     percentage = total / 3

#     # Write all data including total and percentage
#     a.writerow([studentid, rollno, name, mobileno, p1, p2, p3, total, percentage])

# print("Student record has been saved")




