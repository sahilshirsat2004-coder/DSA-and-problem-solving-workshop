# #string is a sequence of characters. In Python, strings are immutable, 
# # which means that once a string is created, it cannot be changed.
# # You can create a string by enclosing characters in single quotes (' '),
# # double quotes (" "), or triple quotes (''' ''' or """ """).

# #array is a collection of items stored at contiguous memory locations.
# # The idea is to store multiple items of the same type together.




# name = "sahilshirsat"
# #indexing
# print(name[0]) #s
# print(name[1]) #a   
# print(name[2]) #h
# print(name[3]) #i
# #print(name[20]) error string index out of range
# print(name[0:5]) #sahil
# print(name[0:]) #sahilshirsat
# print(name[:5]) #sahil
# print(name[0:10:2]) #sihsr
# print(name[::2]) #sihsr
# print(name[1:10:2]) #ahsa
# print(name[1::2]) #ahsa
# print(name[::-1]) #tasrihsilahs



# s="python is a high level programming language"
# print(s.lower()) #pythonis a high level programming language
# print(s.upper()) #PYTHONIS A HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.swapcase()) #PYTHONIS A HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.title()) #Pythonis A High Level Programming Language
# print(s.capitalize()) #Pythonis a high level programming language




# print('subject marks :')
# phy=50
# chem=60
# math=70 

# print("physics ={} chemistry ={} math ={}".format(phy,chem,math))
# print("physics = {0} chemistry = {1} math = {2}".format(phy,chem,math))
# print("physics = {x} ,chemistry = {y} ,math = {z}".format(x=phy,y=chem,z=math))
# total = phy + chem + math
# print("total marks = {}".format(total))
# print("Roll no=","7".zfill(4))



#looping
# for i in range(1,2,11):
#     print(i)



    
# for i in range(1,11):
#     print(i*2)    
    
    
    
    
    
# for i in range(1,11):
#     print(i*2 ,"\t ",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10)    
    
# print()

# for i in range(1,11):
#     print(i*2 ,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10)





# name= "sahilshirsat"
#     #0 1 2 3 4 5 6 7 8 9 10 11
# for i in name: 
#     print(i)
    
    
    
    
# #wap a progran to remove the duplicate characters from the string 
# name= "sahilshirsat"
# new_name = ""

# for i in name:
#     if i not in new_name:
#         new_name += i

# print(new_name)



# for i in range(5,0,-1):
#     print(i)
    
   
   
   
   
    
# for i in range(10,0,-2):
#     print(i)
    
    
    
    
    
# #wap aprogram to reverse a string using for loop

# name= "sahilshirsat"
# reverse_name = ""
# for i in name:
#     reverse_name = i + reverse_name 
# print(reverse_name)



# name= "sahilshirsat"
# n=len(name)
# reverse_name = ""
# for i in range(n-1,-1,-1):
#     reverse_name += name[i]
# print(reverse_name) 



#palimdrome
# string = "madam"
# reverse_string = ""
# for i in string:
#     reverse_string = i + reverse_string
# if string == reverse_string:
#     print("palindrome") 
    
# else:
#         print("not palindrome") 
        
   
   
   
        
# string = "madam"
# print(string)
# print(string[::-1])
# if string == string[::-1]:
#     print("palindrome")
# else:    print("not palindrome")







# mylist = ["sahil", "shirsat", "python", "programming", "language","amol","77","77.77",
#           "True","False"]
# print(type(mylist))
# print(mylist[0]) #sahil
# print(mylist[1]) #shirsat
# print(mylist[2]) #python
# print(mylist[-1]) #False
# print(mylist[2:5]) #python, programming, language
# print(mylist[0:]) #all elements
# print(mylist[:5]) #sahil, shirsat, python, programming, language
# print(mylist[0:10:2]) #sahil, python, language, 77, True
# print(mylist[::2]) #sahil, python, language, 77, True
# print(mylist[1:10:2]) #shirsat, programming, amol, False
# print(mylist[1::2]) #shirsat, programming, amol, False
# print(mylist[::-1]) #False, True, 77.77, 77, amol, language, programming, python, shirsat, sahil
# print(mylist[::]) #sahil, shirsat, python, programming, language, amol, 77, 77.77, True, False

# mylist[2] = "java"
# print (mylist) 

# if "python" in mylist:
#     print("python is present in the list")
# else:    print("python is not present in the list")


# mylist.append("java")
# mylist.append("c++")
# print(mylist)


# mylist.insert(2,"java")
# print(mylist)   

# mylist.remove("python")
# print(mylist)


# newlist = mylist.copy()
# print(newlist)

# mylist = [['sahil','shirsat'],['87','89'],['python','java ']]
# print("example of multidimensional list")
# print(mylist)

# #print(mylist[row][column])
# print(mylist[0][0]) #sahil
# print(mylist[0][1]) #shirsat
# print(mylist[1][0]) #87
# print(mylist[1][1]) #89
# print(mylist[2][0]) #python
# print(mylist[2][1]) #java




# list1= ["sahil","shirsat"]
# print(list1*2) #['sahil', 'shirsat', 'sahil', 'shirsat']

# list2 = [1,2,3,4,5]
# print(list1+list2) #['sahil', 'shirsat', 1, 2, 3, 4, 5]


# list1 = [1,2,3,4,5,'sahil','shirsat']
# del list1[2]
# print(list1) #[1, 2, 4, 5, 'sahil', 'shirsat']


# list1 = [1,2,3,4,5,'sahil','shirsat']
# list1.clear()
# print(list1)



# name= "sahilshirsat"
# print(name)
# myname=list(name)
# print(myname) #['s', 'a', 'h', 'i', 'l', 's', 'h', 'i', 'r', 's', 'a', 't']



# mylist=[1,2,3,4,5,'sahil','shirsat']
# mylist.reverse()
# print(mylist) #['shirsat', 'sahil', 5, 4, 3, 2, 1]


#sorting
# mylist=[5,2,8,1,4]
# mylist.sort()
# print(mylist) #[1, 2, 4, 5, 8]    

#sorting
# mylist=[5,2,8,1,4]
# mylist.sort(reverse=True)
# print(mylist) #[8, 5, 4, 2, 1] 


# mylist=[5,2,8,1,4]
# newlist=mylist
# print(id(mylist)) #140432792
# print(id(newlist)) #140432792
# mylist[0]="sahil"
# print(mylist) #['sahil', 2, 8, 1, 4]
# print(newlist) #['sahil', 2, 8, 1, 4]



# arr = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]

# for i in range(0,4):
#     print(arr[i].pop())


# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for j in range(0,6):
#     print(arr[j],end=" ")
        
        
        
        
# ruit_list1 = ["apple", "banana", "cherry", "papaya"]
# fruit_list2 = fruit_list1
# fruit_list1[0] = "guwaava"
# fruit_list2[1] = "mango"

# sum = 0
# for ls in (fruit_list1, fruit_list2,fruit_list3):
#     for i in ls:
#         sum += 1f




# a=[1,2,3,4,5,6,7,8,9,]
# a[::2]=10,20,30,40,50,60
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1]) 



#tuple is exactly same as list but it is immutable (we cannot change the value of tuple)

# mytuple = ("sahil", "shirsat", "python", "programming", "language","amol","77","77.77",
#             "True","False") 
# print(mytuple) #('sahil', 'shirsat', 'python', 'programming', 'language', 'amol', '77', '77.77', 'True', 'False')
# print(type(mytuple)) #<class 'tuple'>
# print(mytuple[2]) #python



# init_tuple = ()
# print(init_tuple.__len__()) #()

# init_tuple_a ='a','b'
# init_tuple_b = 'a','b'
# print(init_tuple_a==init_tuple_b) #True

# init_tuple_a ='1','2'
# init_tuple_b = '3','4'
# print(init_tuple_a+init_tuple_b) 

# init_tuple_a =('python',)*3
# print(type(init_tuple_a))


# init_tuple=(1,) *3
# init_tuple_a[0]= 2
# print(init_tuple)

# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8])) #7

# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)





# # moves zero in the last
# a =[4,0,2,5,0,1]
# b =[4,2,5,1,0,0]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
        
# print(a)



##remove duplicate elements from the list
# sample_input = [1,2,2,3,4,4,5]
# new_list = []
# for i in sample_input:
#     if i not in new_list:
#         new_list.append(i)  
# print(new_list)



# #common element from the three list
# a=[1,2,3]
# b=[2,3,4]
# c=[3,4,5]

# for i in a:
#     if i in b and i in c:
#      print(i)



# #write a program to calculate and return the sum of distances between the adjecent element in array of positive integer
# n=int(input("enter the size of array: "))
# arr=[]
# for i in range(n):
#     val=int(input("enter the element: "))
#     arr.append(val)
#     sum=0
    
# print(arr)    #[1, 2, 3, 4, 5]
# for i in range(n):
#     if i+1 in range(n):
#         sum+=abs(arr[i]-arr[i+1])
# print(sum)
        
        
        
        
        
# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

# for i in range(1,6):
#     if i==0:
#         continue
#     print(i)


# #zip()  inside wee can use take multiple rannge function
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)
    
    
    
# # wap to move * input= "sahil*shirsat*python*programming*language"
# # output= "****sahilshirsatpythonprogramminglanguage"

# input= "sahil*shirsat*python*programming*language"
# output= ""
# for i in input:
#     if i == "*":
#         output = "*" + output
#     else:
#         output += i  
# print(output)




# # bodmas
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) #160.0
# print((a-b)*(c/d)) #40
# print(a+(b*c)/d)#110.0




# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y) #True
# print(x==z) #False  
# print(x != z) #True




# #wap a program to check if two strings are anagram or not
# string1 = "listen"
# string2 = "silent"
# if sorted(string1) == sorted(string2):
#     print("anagram")
# else:    print("not anagram")


# #counts a word in string
# string = "hello world hello"
# count = 1
# for i in string:
#     if i == " ":
#         count += 1       
# print(count)


# #give an array ,return an array where each element is the product of all the element in the array except itself
# n = int(input("Enter size of array: "))
# arr = []

# for i in range(n):
#     val = int(input("Enter element: "))
#     arr.append(val)

# result = []

# for i in range(n):
#     prod = 1
#     for j in range(n):
#         if i != j:
#             prod *= arr[j]
#     result.append(prod)

# print("Output array:", result)