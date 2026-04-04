# # reaarange positive and negative numbers
# a=[1,2,-2,3,4,56,-7]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:
#         pos.append(i)
        
#     else: 
#         neg.append(i)
# print("positive numbers are:",pos)
# print("negative numbers are:",neg)







# # loigc : Use Moor's voting algorithm to find the majority element.
# #input : [3,3,4,2,4,4,2,4,4]
# #output : 4
# a = [3,3,4,2,4,4,2,4,4]
# candidate = None
# count = 0
# for num in a:
#     if count == 0:
#         candidate = num
#     count += (1 if num == candidate else -1)
# print(candidate)



# #given an array containing positve and negative numbers ,rearranging then into ilternate fashion
# a = [-1,2,-3,4,5,-6]
# b = []
# c = []
# for i in a:
#     if i < 0:
#         b.append(i)
#     else:
#         c.append(i)
# d = []
# for i in range(max(len(b),len(c))):
#     if i < len(b):
#         d.append(b[i])
#     if i < len(c):
#         d.append(c[i])
# print(d)    


# mydict = {
#     101: "prashant",
#     102: "ashish",
#     "103" : "mohini",
#     "104" : "trivani",
#     101: "ashish",
#     104: "ashish"
# }
# print(mydict)

# --------------------------------------------------------------

#with the help of the key we have to print values
# a = mydict[102]
# print(a)

# --------------------------------------------------------------
# we will replace old value with new value
# mydict[102]="peter"
# print(mydict)

# --------------------------------------------------------------
# only print values
# for x in mydict.values():
#     print(x)

# --------------------------------------------------------------
# only print key x=0,1

# for x in mydict():
#     print(x)

# --------------------------------------------------------------
#  print keys and values
# for x,y in mydict.items():
#     print(x,y)

# --------------------------------------------------------------

# if i have to add new value pair in my dictionary

# mydict["mobile_no"] = 234567890
# print(mydict)


# # what will be the output of the following 
# a={'a':1,'b':2,'c':3}
# print(a['a','b'])




# arr={}
# arr[1]=1 
# arr['1']=2
# arr[1] +=1
# print (arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print (sum)






# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)




# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0

# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)






# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))




# dict ={'c':97,'a':96,'b':98}
# for _ in sorted(dict): # pyright: ignore[reportUndefinedVariable]
#     print(dict[_])


# rec={"name":"python","age":"20"}
# r = rec.copy()
# print(id(r)==id(rec))




# rec = {"name":"python","age":"20","addr":"nj","country":"usa"}
# id1=id(rec)
# print (id(id1))
# del rec
# rec = {"Name":"python","age":"20","addr":"nj","country":"usa"}
# id2=id(rec)
# print (id(id2))
# print (id1==id2)




# #write a function find the key with the minimum value in a dictionary
# # input dictionary
# data = {"x": 20, "y": 10, "z": 30}

# # find key with minimum value
# min_key = min(data, key=data.get)

# # print result
# print("Key with minimum value:", min_key)
# print("Minimum value:", data[min_key])




# mydict = {
#     101 : "prashant",
#     "professional": "developer",
#     "empoid": 1001
# }
# mydict.pop(101)    # pop() method remove pair by specific key name
# print(mydict)





# # nested for loop
# for i in range(1,4):           #outerr loop ===> rows
#     for j in range(1,4):       #==>inner loop ==> cols
#         print(i, end=" ")
#     print()




# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()




# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()




# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()



# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+i),end=" ")
#     print()



# def msg():    #call function
#     print("hello world")
    
# msg() #calling funtion

# --------------------------------------------------------------

# def arithmetic():
#     a = int(input("enter value of a"))
#     b = int(input("enter value of b"))
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return add,sub,mul,div

# print(arithmetic())    
# result = arithmetic()
# print("arithmetic", result)






# #positional argument

# def login(username,password):
#     if username==password:
#         print("login sucessfulluy")
#     else:
#         print("invalid credintalds")
        
        
# username=input("enter username:")
# password=input("enter password:")
# login(username,password)





# #keyword argument
# def login(username,password):
#     if username==password:
#         print("login sucessfulluy")
#     else:
#         print("invalid credintalds")
        
   
# login(username="admin",password="admin")




# #default argument
# def cityname(city="goa"):
#     print(city)
    
#     cityname("delhi")
#     cityname("pune")
#     cityname()
    
    
    
# #variable length argument
# def nameofcitys(*city):
#     print("city Name's",city)
    
# nameofcitys("goa","nagpur","pune","satara","sindhudurg")







# #wap for menu driven code 
# import sys
# def add():
#     val1=int(input("enter value for val1:"))
#     val2=int(input("enter value for val2:"))
#     print("add",val1+val2)
    
# def sub():
#     val1=int(input("enter value for val1:"))
#     val2=int(input("enter value for val2:"))
#     print("add",val1-val2)
    
# def mul():
#     val1=int(input("enter value for val1:"))
#     val2=int(input("enter value for val2:"))
#     print("add",val1*val2)

# def div():
#     val1=int(input("enter value for val1:"))
#     val2=int(input("enter value for val2:"))
#     print("add",val1/val2)
    
# while True:
#     print("1. addition")
#     print("2. substraction")
#     print("3. multiplication")
#     print("4. division")
#     print("5.exit")
    
#     choice=int(input("enter your choice:"))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice==4:
#         div()
#     elif choice==5:
#         sys.exit()

    
    
    


# #rstrip()== to remove spaces fron right side
# #lstrip()== to remove spaces at left hand side
# #strip()==  to remove spaces fron=m both sides

# programming =input("enter your progtramming name:")
# p_name = programming.rstrip()
# if p_name=='python':
#     print(p_name)
# elif p_name=='java':
#     print(p_name)
# elif p_name=='cpp':
#     print(p_name)
# else:
#     print("wrong programming name")











