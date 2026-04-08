# #write a program to compress a string by replacing there consecutive charater with there counts

# string = input("Enter string: ")

# output = ""
# count = 1

# for i in range(len(string)):
#     if i < len(string) - 1 and string[i] == string[i + 1]:
#         count += 1
#     else:
#         output += string[i] + str(count)
#         count = 1

# print(output)
# #-------------------------------------------------------------------------------------------------------------------------------


# #write a program to reverse each word of the string

# string = input("Enter string: ")
# output = ""

# for i in range(len(string) - 1, -1, -1):
#     output += string[i]

# print(output)


#-------------------------------------------------------------------------------------------------------------------------------

# #abstraction
# from abc import ABC, abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass
    
#     @abstractmethod
#     def placement(self):
#         pass
    
# class Ashish(Help4code):
#     def training(self):
#         print("c,c++,java")
#     def placement(self):
#         print("java placement")
        
# class Ankush(Help4code):
#     def training(self):
#         print("python,java")
#     def placement(self):
#         print("python placement")
        
# class Prashant(Help4code):
#     def training(self):
#         print("machine learning")
#     def placement(self):
#         print("data science placement")
        

# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Prashant()
# obj3.training()
# obj3.placement()


#-------------------------------------------------------------------------------------------------------------------------------

# from abc import ABC, abstractmethod

# class irctc(ABC):   # fixed name
#     @abstractmethod
#     def book_ticket(self):
#         pass

# class makemytrip(irctc):
#     def book_ticket(self):
#         print("===== MakemyTrip =====")
#         input("Enter source: ")
#         input("Enter destination: ")
#         input("Enter date: ")
#         print("======================")

# class goibibo(irctc):
#     def book_ticket(self):
#         print("===== Goibibo =====")
#         input("Enter source: ")
#         input("Enter destination: ")
#         input("Enter date: ")
#         print("===================")

# class yatra(irctc):
#     def book_ticket(self):
#         print("===== Yatra =====")
#         input("Enter source: ")
#         input("Enter destination: ")
#         input("Enter date: ")
#         print("=================")

# # objects
# makemytrip().book_ticket()
# goibibo().book_ticket()
# yatra().book_ticket()



#-------------------------------------------------------------------------------------------------------------------------------
# class Base:
#     def __init__(self):
#         print("parent class constructor called")
#         self.a = "sahil shirsat"
#         self._c = "cse"

# class Derived(Base):
#     def __init__(self):
#         print("child class constructor called")
#         Base.__init__(self)   # calling parent constructor
#         print(self.a)
#         print(self._c)

# obj = Derived()
# print(obj.a)
# print(obj._c)


#-------------------------------------------------------------------------------------------------------------------------------

# class Rbi:
#     def publicPolicy(self):
#         print("check the public policy of rbi")
        
#     def __privatePolicy(self):
#         print("this is private policy")

#     def accessPrivate(self):   # helper method
#         self.__privatePolicy()

# class Sbi(Rbi):
#     def __init__(self):
#         super().__init__()
    
#     def callingPublicMethod(self):
#         print("\nInside child class")
#         self.publicPolicy()
        
#     def callingPrivateMethod(self):
#         print("\nInside child class")
#         # self.__privatePolicy() ❌ not allowed
#         self.accessPrivate()   # ✅ correct way

# # object
# obj = Sbi()
# obj.callingPublicMethod()
# obj.callingPrivateMethod()

# # parent object
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.accessPrivate()



# # obj1 = Sbi()
# # obj1.callingPublicMethod()
# # obj1.callingPrivateMethod()
# # obj1.publicPolicy()
# # obj1.__privatePolicy()
# # obj2 = Rbi()
# # obj2.publicPolicy()
# # obj2.__privatePolicy()
# # obj2 = Rbi()
# # obj2.publicPolicy()
# # obj2.Rbi_privatePolicy()


#---------------------------------------------------------------------------------------------

# #move all even numbers first, then all odd numbers, while preserving order if needed

# n = int(input("Enter number of elements: "))
# arr = list(map(int, input("Enter numbers: ").split()))

# even = []
# odd = []

# for num in arr:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print(*(even + odd))


#---------------------------------------------------------------------------------------------
#DSA

# # stack data structure inplementation without ssize limit
# import sys
# class Stack:
#     def _init_(self, stackSize):
#         self.stacklist = []
#         self.stackSize = stackSize
        
#     def isFull(self):
#         if len(self.stacklist) == self.stackSize:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.stacklist.append(value)

#     def display(self):
#         print("---------------------------")
#         print(self.stacklist)
#         print("---------------------------")

#     def isEmpty(self):
#         if self.stacklist == []:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist.pop()
        
#     def delete(self):
#         self.stacklist = None
#         print("stack is deleted")

#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist[-1]
        

# size = int(input("Enter the size of the stack: "))
# stackobj =  Stack(size)

# while True:
    
#     print("1.push element")
#     print("2.display stack element")
#     print("3. check isEmpty")
#     print("4.pop element")
#     print("5.delete stack")
#     print("6.peek operation")
#     print("7.Exit")



#     choice = int(input("enter your choice:"))
#     if choice == 1 :
#         val= int(input("enter the value for stack:"))
#         stackobj.push(val)

#     elif choice == 2:
#         stackobj.display()
    
#     elif choice == 3:
#        print(stackobj.isEmpty())
    
#     elif choice == 4:
#         print(stackobj.pop())

#     elif choice == 5:
#         stackobj.delete()

#     elif choice == 6:
#         stackobj.peek()
    
#     elif choice == 7:
#         sys.exit()
#     else:
#             print("Invalid choice, please try again.")



#---------------------------------------------------------------------------------


# import sys
# class Stack:
#     def _init_(self, stackSize):
#         self.stacklist = []
#         self.stackSize = stackSize
        
#     def isFull(self):
#         if len(self.stacklist) == self.stackSize:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.stacklist.append(value)

#     def display(self):
#         print("---------------------------")
#         print(self.stacklist)
#         print("---------------------------")

#     def isEmpty(self):
#         if self.stacklist == []:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist.pop()
        
#     def delete(self):
#         self.stacklist = None
#         print("stack is deleted")

#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.stacklist[-1]
        

# size = int(input("Enter the size of the stack: "))
# stackobj =  Stack(size)

# while True:
    
#     print("1.push element")
#     print("2.display stack element")
#     print("3. check isEmpty")
#     print("4.pop element")
#     print("5.delete stack")
#     print("6.peek operation")
#     print("7.Exit")



#     choice = int(input("enter your choice:"))
#     if choice == 1 :
#         val= int(input("enter the value for stack:"))
#         stackobj.push(val)

#     elif choice == 2:
#         stackobj.display()
    
#     elif choice == 3:
#        print(stackobj.isEmpty())
    
#     elif choice == 4:
#         print(stackobj.pop())

#     elif choice == 5:
#         stackobj.delete()

#     elif choice == 6:
#         stackobj.peek()
    
#     elif choice == 7:
#         sys.exit()
#     else:
#             print("Invalid choice, please try again.")
            
            
            
            
            
#--------------------------------------------------------------------------------


# import time

# class TowerOfHanoi:
#     def _init_(self, source):
#         self.A = source[:]   # source
#         self.B = []          # auxiliary
#         self.C = []          # destination
#         self.n = len(source)

#     def display(self):
#         print(f"A: {self.A}   B: {self.B}   C: {self.C}")
#         print("-" * 40)
#         time.sleep(1)  # delay (1 second)

#     def move_disk(self, from_rod, to_rod, from_name, to_name):
#         if not from_rod:
#             disk = to_rod.pop()
#             from_rod.append(disk)
#             print(f"Move disk {disk} from {to_name} → {from_name}")
#         elif not to_rod:
#             disk = from_rod.pop()
#             to_rod.append(disk)
#             print(f"Move disk {disk} from {from_name} → {to_name}")
#         elif from_rod[-1] > to_rod[-1]:
#             disk = to_rod.pop()
#             from_rod.append(disk)
#             print(f"Move disk {disk} from {to_name} → {from_name}")
#         else:
#             disk = from_rod.pop()
#             to_rod.append(disk)
#             print(f"Move disk {disk} from {from_name} → {to_name}")

#         self.display()  # show state after every move

#     def solve(self):
#         print("Initial State:")
#         self.display()

#         s, a, d = 'A', 'B', 'C'

#         if self.n % 2 == 0:
#             a, d = d, a

#         total_moves = 2 ** self.n - 1

#         for i in range(1, total_moves + 1):
#             if i % 3 == 1:
#                 self.move_disk(self.A, self.C, s, d)
#             elif i % 3 == 2:
#                 self.move_disk(self.A, self.B, s, a)
#             else:
#                 self.move_disk(self.B, self.C, a, d)

#         print("Final State:")
#         self.display()


#---------------------------------------------------------------------------


# import sys 
# class Tower:
#     def _init_(self):
#         print("Tower of Hanoi")
#         print()
#         print("given problem   A=[3,2,1], B = [], C = []")
#         print()
#         print("expected output A =[], B =[] , C =[3,2,1]")
#         self.A = []
#         self.B = []
#         self.C = []
#         self.D = []

#     def tower(self,item):
#         self.A.append(item)
#         print("A = ",self.A)
#         print("Items in Tower A\n")

#     def pass1(self):
#         self.temp = self.A.pop(2) #a=[3,2]
#         self.c.append(self.temp) #c = [1] =>temp
        