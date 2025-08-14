# class Student():
#     def __init__(s):
#         print("Hello")
# s=Student()


# class Student():
#     def __init__(self,name,age):
#         self.sname=name
#         self.sage=age
    
# s=Student("sai",21)
# print(s.sname)
# print(s.sage)


# def display():
#     a=50
#     b=50
#     print(a+b)
# display()

# def dis(val):
#     return(val)
# x=dis("sai")
# print(x)


#function without parameter
# def add():
#     a=50
#     b=50
#     print(a+b)
# add()

#return type function without parameter
# def display():
#     return "welcome"
# x=display()
# print(x)

#

# def d(a,b,c):#
#     res=a+b+c
#     return res

# x=d(10,20,50)
# print(x)


# def fruits_list(lst):
#     print(lst)


# f=["orange","Apple"]
# fruits_list(f)


#var-arg
#variable - aruguments:
#*args

# def add(*args):
#     print(args)

# add(21,6,64,4,654,54,5,5,)
# add(20)
# add(21654,665,4,64)


# def add(a):
#     print(a)
# add(20)
# add(40)
# add(70)


# class Student:
#     college="SRU"
#     def __init__(self,n,):
#         self.n=n

#         print("welcome",self.college)

#     def display(self,name2):
#         self.name2=name2

#         print(self.n)
#         print(self.name2)

# s=Student("sai")
# print(s.college)
# s.display("arun")

# s1=Student("rohith")
# print(s1.college)
# s1.display("hekk")


# s2=Student("rohith")
# print(s2.college)
# s2.display("arun")

# class Restaurent:
#     name="Babai Hotel"

#     def __init__(self,foodname,price):
#         self.foodname=foodname
#         self.price=price
        
#     def display(self):
#         print("Restaurent=",self.name)
#         print("foodname=",self.foodname)
#         print("price=",self.price)

# o=Restaurent("chapathi",100)
# o.display()

# r=Restaurent("chicken fry",1000)
# r.display()

#problem 1
# n=int(input())
# no=int(input())
# c=0
# for i in range(n):
#     x=int(input())
#     if x%no==0:
#         c+=1
# print(c)


#Node creation
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertatend(self,data):#data=30
#         newnode=Node(data)#newnode=3000

#         if self.head is None:
#             self.head=newnode
#         else:
#             temp=self.head

#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=newnode

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="---->")
#             temp=temp.next
        
# l=LinkedList()
# l.insertatend(10)
# l.insertatend(20)
# l.insertatend(30)
# l.insertatend(40)

# l.display()


#insert at begin
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
        
# class Linkedlist:
#     def __init__(self):
#         self.head=None

#     def insertAtBegin(self,data):
#         newnode=Node(data)

#         if self.head is None:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head=newnode

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="---->")
#             temp=temp.next


# l=Linkedlist()
# l.insertAtBegin(10)
# l.insertAtBegin(20)
# l.insertAtBegin(33)
# l.display()


#insert at specfic posistion


# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertatend(self,data):#data=30
#         newnode=Node(data)#newnode=3000

#         if self.head is None:
#             self.head=newnode
#         else:
#             temp=self.head

#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=newnode

#     def insertatpos(self,pos,data):
#         newnode=Node(data)
#         if pos==0:
#             newnode.next=self.head
#             self.head=newnode
#         else:
#             temp=self.head
#             for i in range(1,pos):
#                 temp=temp.next
#             newnode.next=temp.next
#             temp.next=newnode

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="---->")
#             temp=temp.next
        
        
# l=LinkedList()
# l.insertatend(10)
# l.insertatend(20)
# l.insertatend(30)
# l.insertatend(40)
# print("before insert")
# l.display()
# pos=2
# l.insertatpos(pos,60)
# print("after insert")
# l.display()


# prac
# class Node:
#     def __init__(self,val):
#         self.head=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def insertatend(self,data):
#         newnode=Node(data)

#         if self.head is None:
#             self.head=newnode
#         else:
#             temp=self.head
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=newnode

#     def insertatbegin(self,data):
#         newnode=Node(data)

#         if self.head is None:
#             self.head=newnode
#         else :
#             newnode.next=self.head
#             self.head=newnode

    






# l=LinkedList()
# l.insertatend(10)

#at mid posistion 
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertatend(self,data):#data=30
#         newnode=Node(data)#newnode=3000

#         if self.head is None:
#             self.head=newnode
#         else:
#             temp=self.head

#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=newnode

#     def insertatpos(self,pos,data):
#         newnode=Node(data)
#         if pos==0:
#             newnode.next=self.head
#             self.head=newnode
#         else:
#             temp=self.head
#             for i in range(1,pos):
#                 temp=temp.next
#             newnode.next=temp.next
#             temp.next=newnode

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="---->")
#             temp=temp.next
        
'''# li=[]       
# l=LinkedList()
# li.append(l.insertatend(10))
# li.append(l.insertatend(20))
# li.append(l.insertatend(30))
# li.append(l.insertatend(40))
# li.append(l.insertatend(50))
# li.append(l.insertatend(60))
# li.append(l.insertatend(70))
# li.append(l.insertatend(80))
# print("before insert")
# l.display()
# length=len((li))
# mid=length//2
# pos=mid
# l.insertatpos(mid,100)
# print("after insert")
# l.display()'''

# l2=[]
# l=LinkedList()
# n=int(input())
# for i in range(n):
#     x=int(input())
#     r=l.insertatend(x)
#     l2.append(r)
# print("before insert")
# l.display()
# length=len((l2))
# mid=length//2
# pos=mid
# l.insertatpos(mid,100)
# print("after insert")
# l.display()



# delection at begin
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertatend(self,data):#data=30
#         newnode=Node(data)#newnode=3000

#         if self.head is None:
#             self.head=newnode
#         else:
#             temp=self.head

#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=newnode
    
#     def deleteatBegin(self):
#         if self.head is None:
#             print("List is Empty")
#         else:
#             self.head=self.head.next

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="-->")
#             temp=temp.next
        
        
# l=LinkedList()
# num=int(input())
# for i in range(num):
#     data=int(input())
#     l.insertatend(data)
# print("before delete")
# l.display()
# l.deleteatBegin()
# print("after delete")
# l.display()

 
 #delete end
 
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
    
# class LinkedList:
#     def __init__(self):
#         self.head=None
    
#     def insertbegin(self,data):
#         newnode=Node(data)

#         if self.head is None:
#             self.head=newnode
#         else:
#             newnode.next=self.head
#             self.head=newnode
    
#     def deleteatend(self):
#         if self.head is None:
#             print("List is empty")
#         elif self.head.next is None:
#             self.head=None
#         else:
#             temp=self.head
#             while temp.next.next is not None:
#                 temp=temp.next
#             del temp.next
#             temp.next=None
        

#     def display(self):
#         temp = self.head
#         if self.head is None:
#             print("List is Empty")
#         while temp is not None:
#             print(temp.data, end="-->")
#             temp = temp.next
        
# l=LinkedList()
# num=int(input())
# for i in range(num):
#     data=int(input())
#     l.insertbegin(data)
# print("before delete")
# l.display()
# l.deleteatend()
# print('\n',"after delete")
# l.display()


#delete position
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbegin(self,data):
        newnode=Node(data)
        if self.head  is None :
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="-->")
                temp=temp.next

    def deleteAtPos(self,pos):
        if self.head is not None:
            if pos==1:
                temp=self.head
                self.head=self.head.next
                del temp
            else:
                temp=self.head
                prev=None
                for i in range(1,pos):
                    prev=temp
                    temp=temp.next
                prev.next=temp.next
                del temp



l=Linkedlist()
num=int(input())
for i in range(num):
    x=int(input())
    l.insertatbegin(x)
print("Before Delete")
l.display()
print("After delete")
pos=int(input("\n"))
l.deleteAtPos(pos)
l.display()