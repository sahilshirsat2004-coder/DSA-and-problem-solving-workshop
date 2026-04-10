# dict={
#     "c":3,
#     "B":2,
#     "A":1
# }
# B={}

# A=sorted(dict.items())
# print(A)

# B=sorted(dict.items(),reverse=True)
# print(B)

#Q2:
# A={"A":1,"B":2,"C":3}

# B= A.clear()
# print(B)





# import sys
# class Queue:
#     def __init__(self,queueSize):
#         self.queueList =[] # Queue created
#         self.queueSize = queueSize
        
#     def isFull(self):
#         if len(self.queueList)== self.queueSize:
#             return True
#         else: 
#             return False
        
#     def Enqueue(self, value):
#         if self.isFull():
#             print("Queue is full")
            
#         else:
#             self.queueList.append(value)
            
        
        
#     def displayQueue(self):
#         print(self.queueList)
        
#     def isEmpty(self):
#         if self.queueList ==[]:
#             return True
#         else:
#             return False
        
#     def Dequeue(self):
#         if self.isEmpty():
#             print("Queue is empty:")
#         else:
#            return self.queueList.pop()
       
#     def deleteQueue(self): # delete the queue
#         self.queueList = []
#         return "Queue is deleted"
    
#     def peek(self): #it return the first element of Queue
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             return self.queueList[0] # slicing of list
        
    
        
# size = int(input("Enter the size of Queue : ")) 
# print()
# print("Queue has been created with size ",size)      
# queueObj = Queue(size) # Queue object has created 
        

# while True:
#     1
    
#     print("1.Enqueue element in Queue ")
#     print("2.Display Queue element")
#     print("3.Check Queue IsEmpty ")
#     print("4.Pop Operation")
#     print("5.Delect full Queue")
#     print("6.Peek Operation")
#     print("7.Exit from system")
    
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#        val = int(input("Enter the value for stack : "))
#        queueObj.Enqueue(val)
#     elif choice ==2:
#         queueObj.displayQueue()
        
#     elif choice ==3:
#         print(queueObj.isEmpty())
        
#     elif choice == 4:
#         print(queueObj.Dequeue())
        
#     elif choice == 5:
#         print(queueObj.deleteQueue())
        
#     elif choice == 6:
#         print(queueObj.peek())
        
#     elif choice == 7:
#         sys.exit()









# time complexity -
# 0(1) represents constant time

# Big O Notation
# O(1)        -   Constant Time       -   Accessing a specific eleement in array
# O(n)        -   Linear Time         -   Loop through array elements
# O(log n)    -   Logarithmic Time    -   Find an element in sorted array
# O(n^2)      -   Quadratic Time      -   Looking at every index in the array twice
# O(2^n)      -   Exponential Time    -   Double recursion in Fibonacci
# O(n log n)  -   Log-Linear Time     -   Merge Sort

# O(1) - Constant Time
# array = [1,2,3,4,5]
# array[0] //It takes constant time to access first element

# O(n) - Linear Time
# array = [1,2,3,4,5]
# for element in array:
#     print(element)) //Linear time since it is visiting every element of the array4


# O(LogN)-Logarithmic time
# array = [1,2,3,4,5]
# for index in range(0, len(array), 3):
#     print(array[index])
#     //Logarithmic time since it is visiting only some elements

# O(N^2)-Quadratic time 
# array = [1,2,3,4,5]

# for x in array:
#     for y in array:
#         print(x,y)

# O(2^N)-Exponential time
# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-1)

                                   # Time Complexity             Space Complexity
# Create Stack                             O(1)                        O(1)
# Push                                 O(1)/O(n^2)                     O(1)
# Pop                                      O(1)                        O(1)
# Peek                                     O(1)                        O(1)
# isEmpty                                  O(1)                        O(1)
# Delete Entire Stack                      O(1)                        O(1)



# There are 2 ways to implement stack : 1) Array 2)Linked list

# stack using list
#      - Easy to implement
#      - Speed problem when it grows

# stack using linked list
#      - Faster performance 
#      - Implementation is not easy



#                             Time Complexity     Space Complexity
# Create Queue                      O(1)                 O(1)
# Enqueue                           O(n)                 O(1)
# Dequeue                           O(n)                 O(1)
# Peek                              O(1)                 O(1)
# isEmpty                           O(1)                 O(1)
# Delete Entire Queue               O(1)                 O(1)


# queue using list
#     -easy to implement
#       -speed problem when it grow

# queue using linked list
#       - fast performance
        # - implementation is not easy

# def FindBiggestNumber(array):
#     firstvalue=array[0]
#     for i in range(1,len(array)):
#         if array[i]>firstvalue:
#             firstvalue=array[i]
#     return firstvalue
# array=[1,2,3,4,5]
# print(FindBiggestNumber(array))


# def findBiggestNumber(array):------------------->O(1)
#     firstvalue=array[0]------------------------->O(1)
#     for i in range(1,len(array)):--------------->O(n)----->
#         if array[i]>firstvalue:----------------->O(1)----->O(n) #overall complexity is the O(n)
#             firstvalue=array[i]----------------->O(1)----->
#     print(firstvalue)--------------------------->O(1)
    
# array=[2,4,5,6,7,1,9,3,4,5,6]
# findBiggestNumber(array)


# A="gasgg54@#vscsd$#"
# count=0

# for i in A:
#     if not i.isalnum():
#         count+=1

# print(count)






# # A=[79,77,54,81,48,34,25,16]

# import math

# A=[79,77,54,81,48,34,25,16]
# Count=0 
# for i in A:
#     if math.sqrt(i)==math.sqrt(i)//1:
#         Count+=1
# print("the total square plots are ",Count)





# def linearSearch(array,target):    #array=[1,2,3,4,5,6,7,8,9]
# #     for i in range(len(array)): # ===================>o(n)
# #         if array[i]==target:        # ===================>o(1)
# #             return i
# #     return -1
    


# # array=[1,2,3,4,5,6,7,8,9]
# # target=5
# # result=linearSearch(array,target)
# # if result == -1:
# #     print("not found")
# # else:
# #     print("element found at index no=",result)


# def binarysearch(array,target):
#     start=0
#     end=len(array)-1
#     while start <=end:
#         mid=start+end
#         if array[mid]==target:
#             return mid 
#         elif array[mid]<target:
#             start = mid+1
#         else:
#             end=mid-1
#     return -1


# sortedArray=[1,2,3,4,5,6,7,8,9]
# target =5
# result= binarysearch(sortedArray,target)    
# if  result==-1:
#     print("element not found")
# else:
#     print("element found at index",result)






# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next=None
        
# class LinkedList:
#     def __init__(self):
#         self.head =None

# linkedlist = LinkedList()


# linkedlist.head= Node(5)
# second          =Node(10)
# third           =Node(15)
# fourth          =Node(20)

# print(linkedlist.head.data)
# print(second.data)
# print(third.data)
# print(fourth.data)


# print(linkedlist.head.next)
# print(second.next)
# print(third.next)
# print(fourth.next)

# linkedlist.head.next=second
# second.next=third
# third.next=fourth





# #linking part

# linkedlist.head.next = second
# second.next=third


# #display linkedlist

# while linkedlist.head != None:
#     print("|",linkedlist.head.data,"|",linkedlist.head.next,"->",end=" ")
#     linkedlist.head=linkedlist.head.next




# import sys
# class Node:
#     def __init__(self):
#         self.data=data #instance variable
#         self.next = None



# class Linkedlist:
#     def __init__(self):
#         self.head =None
#         self.tail =None


#     def addNode(self,value):
#         node = Node(value)
#         if self.head is None:

#             self.head= node
#             self.head=node
#         else:
#             self.tail.next= node
#             self.tail =node



# if __name__=='__main__':
#     object = Linkedlist()

#     #menu driven option
#     ''
#     while True:
#         print("1.add node linkedlist:")
#         print("2.add node in beginning:")
#         print("3.add node in between:")
#         print("4.add node end:")
#         print("5.display linked list")
#         print("6.exit")

#         ch=int(input("enter your choice:"))

#         if ch == 1:
#             Value = int(input("enter the value for node:"))
#             object.addNode(Value)
#             print("Node added successfully in single linkedlist")








