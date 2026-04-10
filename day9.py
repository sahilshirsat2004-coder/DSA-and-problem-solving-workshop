#no stack memory is required in case if iteration
#stack memory is required in case of recursion
#stack memory is required in case of loop

#in case if recursion system needs more time for pop and push elements tostack memory which makes recursion less time efficient

#we use recursion especially in the cases we know that the problem can be divided into smaller subproblems


# def powerofTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerofTwo(n-1)
#         return 2 * power

    
# def powerofTwo(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i += 1
#     return power



# def powerOfTwo(n):
#     if n==0:
#         return 1
#     else:
#         return 2*powerOfTwo(n-1)
    
    
    


# #factorial solution
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))





# #palindrome using recursion
# def isPalindrome(string):
#     if len(string)==0:
#         return True 
#     if string[0]!=string[-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome("madam"))


  





# #power
# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base,exponent-1)
    
# print(power(2,3))





# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)

#     def __str__(self, level=0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret


# # object creation
# rootNode = Tree("root")
# hot = Tree("hot")
# cold = Tree("cold")
# tea = Tree("tea")
# coffee = Tree("coffee")
# nonAlcoholic = Tree("nonAlcoholic")
# alcoholic = Tree("alcoholic")

# # add child nodes
# rootNode.add_child(hot)
# rootNode.add_child(cold)

# hot.add_child(tea)
# hot.add_child(coffee)

# cold.add_child(alcoholic)
# cold.add_child(nonAlcoholic)

# # print tree
# print(rootNode)






# class Tree:
    
#     def _init_(self,data):
#         self.data = data
#         self.children = []
    
#     def addChild(self,child):
#         self.children.append(child)
           
#     def _str_(self,level=0):
#         ret = "  " * level + str(self.data)+"\n"
#         for child in self.children:
#             ret+=child._str_(level+1)
#         return ret
    
# rootNode=Tree("N1")

# N2=Tree("N2")
# N3=Tree("N3")
# N4=Tree("N4")
# N5=Tree("N5")
# N6=Tree("N6")
# n7=Tree("N7")
# N8=Tree("N8")
# N9=Tree("N9")
# N10=Tree("N10")

# rootNode.addChild(N2)
# rootNode.addChild(N3)

# N2.addChild(N4)
# N2.addChild(N5)

# N3.addChild(N6)
# N3.addChild(n7)

# N4.addChild(N9)
# N4.addChild(N10)

# print(rootNode)






# #perfect binary tree
# #all internal nodes have exactly two child nodes
# #all leaf nodes are at the same level



