# s=Stack()
# num=int(input())
# for i in range(num):
#     data=int(input())
#     s.push(data)
# s.display()
# print(s.isEmpty)
# print(s.peel())
# print(s.pop())
# print(s.peek())
# s.display()


#encapsulation

# class Bank:
#     __accno=""
#     __bal=0
# #setter method-->assign value to access private data
#     def setAccno(self,num):
#         self.__accno=num
#     def setbal(self,num):
#         self.__bal=num
# #getter method --->getting to access private data 
#     def getAccno(self):
#         return self.__accno
#     def getbal(self):
#         return self.__bal
# b=Bank()
# b.setAccno(111)
# print(b.getAccno())

# b.setbal(1230)
# print(b.getbal())


# class Bank:
#     __accno=""
#     __balance=0.00

#     def __init__(self,num,bal):
#         self.__accno=num
#         self.__balance=bal

#     def setBal(self,bal):
#         self.__balance=bal
        
#     def getBal(self):
#         return self.__balance
    
#     #setter method----->assign value to private
#     def setAccno(self,num):
#         self.__accno=num

#     #getter method --->getting private data
#     def getAc

# # Polymorphism 
# # Polymorphism means "many forms" - the same method or function name can behave differently based on the object that is calling it.
# # Types of Polymorphism in python compiled time polymorphism method overloading runtime polymorphism method overriding 1 method overloading compile time polymerism method overloading means having multiple methods within the same name but different parameter same method name same class different parameter in the

# class payment :
# def pay(crerZf$aZ!A1

# arr=[2,4,2,7,2,9]
# target=2
# l=[]
# for i in range(len(arr)):
#     if arr[i]==target:
#         l.append(i)
# print(l)


#recursion:
#function of copy caalling again and again itself 
#1.base case-->terminate the recursion
#resursive case

# def display(a):
#     if a>10:
#         return
#     else:
#         print(a)
#         a=a+1
#         display(a)
# display(1)

# num=5
# fact=1
# for i in range(1,num+1):
#     fact*=i
#     print(fact)


def fact(n):
    if n==0  or n==1:
        return 1
    return n*fact(n-1)
fact(5)