
#STACK
# A stack is a linear data structure that follows the LIFO principle:
# last in first out the last 
# element added is the 1st one to be removed

#stack operations
#push
#pop
#peek
#isEmpty

#List:

# class Stack:
#     def __init__(self):
#         self.lst=[]

#     def isEmpty(self):
#         size=len(self.lst)
#         return size==0
#     def push(self,data):
#         self.lst.append(data)
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#             return
#         return self.lst.pop()
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#             return
#         return self.lst[-1]
#     def __str__(self):
#         return f"Stack is {self.lst}"
    
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s)
# print(s.isEmpty())
# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s)


class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return
        v=self.head.data
        self.head=self.head.next
        return v
    def peek (self):
        if self.head is None:
            print("Stack is empty")
            return
        return self.head.data
    def isEmpty(self):
        return self.head is None
    
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
s=Stack()
num=int(input())
for i in range(num):
    data=int(input())
    s.push(data)
s.display()
print(s.isEmpty())
print(s.peek())
print(s.pop())
print(s.peek())
s.display()