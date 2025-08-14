#inheritance 
#parent class or base or super class
#child class or derived class or sub class

# class Student:#parent class
#     name="mathi"
#     rollno=25

# class Report(Student):#child class
#     cgpa=99.99
# r=Report()
# print(r.name)
# print(r.rollno)

#eg2
# class Student:
#     cname="SRU"
#     name="mathi"
#     rnum=25
#     def display(self):
#         print(self.cname)
#         print(self.name,self.rnum)

# class Report(Student):
#     cgpa=99.99
#     def show(self):
#         print("CGPA:",self.cgpa)

# o=Report()
# o.display()
# o.show()

#eg3
# class Account:#parent class
#     bank_name="SBI"
#     cus_name="mathi"
#     accno=111
#     init_balance=10000

#     def display(self):
#         print(f"Bank NAme:{self.bank_name}")
#         print(f"Customer Name: {self.cus_name}")
#         print(f"Account no:{self.accno}")
#         print(f"balance:{self.init_balance}")

# class Deposit(Account):
#     Deposit=5000
#     def show(self):
#         self.init_balance=self.init_balance+self.Deposit
#         print(f"Balance:{self.init_balance}")

# o=Deposit()
# o.display()
# o.show()



#single inheritance
#2 parent single child class


# class Friend1:
#     food="chicken biryani"
# class Friend2:
#     food2="grill chicken"

# class You(Friend1,Friend2):
#     def eat(self):
#         print("you can eat both")
#         print(f"friend 1 :{self.food}")
#         print(f"friend 2:{self.food}")

# c=You()
# c.eat()

#Multilevel Inheritance
#multilevel inheritance means a class is derived from a class which is also from another class

# class A:
#     name="mathi"
# class B(A):
#     cgpa=80.89
# class C(B):
#     marks=65

# o=C()
# print(o.name)
# print(o.cgpa)

#eg2
# class Student:
#     name="mathi"
#     rnum=25
# class Attendance(Student):
#     present=60
# class Report(Attendance):
#     cgpa=99.99
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Roll No:{self.rnum}")
#         print(f"Present days:{self.present}")
#         print(f"CGPA:{self.cgpa}")

# o=Report()
# o.display()


# Hierarchical inheritance
# Hierarchical inheritance means multiple subclasses inherit From a single parent class
# It's like one base class (parent) gives its properties to many child classes

# class A:
#     name="mathi"
# class B(A):
#     cgpa=99.99
# class C(A):
#     present=60

# class Account:
#     name="mathi"
#     accno=111
#     init_bal=10000


# class Deposit(Account):

#     deposit=2000
#     def show(self):
#         self.init_bal+=self.deposit
#         print(f"Account:{self.accno}")
#         print(f"balance:{self.init_bal}")

# class Withdraw(Account):
#     withdraw=1000
#     def display(self):
#         self.init_bal-=self.withdraw
#         print(f"Accno:{self.accno}")
#         print(f"balance:{self.init_bal}")

# d=Deposit()
# d.show()
# W=Withdraw()
# print("After withdraw")
# W.display()
    

# Hybrid inheritance hybrid inheritance is a combination of two or more types of inheritance such as
# Single 
# multiple
# multilevel
#  hierarchical



# Super 
# Super()
# is a inbuilt function in python used to call methods from a parent (super)class.
#  it is his most commonly used in inheritance to:
#  call the constructor of the parent class 
# call methods from the parent class inside a child class

# class Student:
#     def __init__(self,name):
#         self.sname=name
#         print(f"Student Parent: {self.sname}")

# class Report(Student):
#     def __init__(self,name,cgpa):
#         super().__init__(name)
#         self.scgpa=cgpa
#         print(f"CGPA:{self.scgpa}")

# o=Report("mathi",99.99)


# class Student:
#     def __init__(self,name,rnum):
#         self.sname=name
#         self.srnum=rnum

# class Report(Student):
#     def __init__(self,name,rnum,cgpa):
#         super().__init__(name,rnum)
#         self.scgpa=cgpa

#     def display(self):
#         print(f"Name:{self.sname}")
#         print(f"Roll no:{self.srnum}")
#         print(f"CGPA:{self.scgpa}")

# name=input()
# rnum=int(input())
# cgpa=float(input())
# r=Report(name,rnum,cgpa)
# r.display()

#q
# class A:
#     def __init(self):
#         print("Class A")
# class B:
#     def __init__(self):
#         super().__init__()
#         print("Class B")
# class C:
#     def __init__(self):
#         super().__init__()
#         print("Class C")



#DOUBLE LINKEDLIST

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insertatend(self,data):
        Newnode=Node(data)
        if self.head is None:
            self.head=Newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=Newnode
            Newnode.prev=temp
        
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="--->")
            temp=temp.next
    
    def backward(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        while temp is not None:
            print(temp.data,end="--->")
            temp=temp.prev

o=DoublyLinkedList()
num=int(input())
for i in range(num):
    s=input().split(" ")
    if s[0]=="insertAtEnd":
        o.insertatend(s[1])
    elif s[0]=="display":
        o.display()
        print("\nBackward direction")
        o.backward()

# o=DoublyLinkedList()
# o.insertatend(10)
# o.insertatend(20)
# o.insertatend(30)
# o.display()