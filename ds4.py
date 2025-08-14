#doulble linked list
#insertatbegin
#insertatend
#deleteatbegin
#deleteatbegin


# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
#         self.prev=None

# class DoubleLinkedList:
#     def __init__(self):
#         self.head=None
    
#     def insertatbegin(self,data):
#         newnode=Node(data)

#         if self.head is None:
#             self.head=newnode
#         else :
#             newnode.next=self.head
#             self.head.prev=newnode
#             self.head=newnode

#     def deleteatbegin(self):

#         if self.head is None:
#             print("List is empty")
        
#         elif self.head.next is None:
#             self.head=None
#         else:
#             self.head=self.head.next
#             self.head.prev=None

#     def deleteatend(self):
#         if self.head is None:
#             print("List is empty")
#         elif self.head.next is None:
#             self.head=None
#         else:
#             temp=self.head
#             while temp.next.next is not None:
#                 temp=temp.next
#             temp.next=None

#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="--->")
#             temp=temp.next

#     def backward(self):
#         temp=self.head
#         while temp.next is not None:
#             temp=temp.next
#         while temp is not None:
#             print(temp.data,end="--->")
#             temp=temp.prev
    
    
        
# d1=DoubleLinkedList()
# num=int(input())
# for i in range(num):
#     data=int(input())
#     d1.insertatbegin(data)
# d1.display()
# print("\nBackward ")
# d1.backward()
# print("\nafter deleteing at begin")
# d1.deleteatbegin()
# d1.display()
# d1.deleteatend()
# print("")
# d1.display()

#circular linked list
# Circular linker list is a linked list where the last node points back to the first node,
# forming a circle 
# It has no null (None) at the end.

#operations
#insertatbegin
#insertatend
#deleteatbegin
#deleteatbegin

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class CircularList:
    def __init__(self):
        self.head=None

    def insertatend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head


    def insertatbegin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            newnode.next=self.head
            self.head=newnode
            temp.next=self.head

    def display(self):
        temp=self.head
        while temp.next is not self.head :
            print(temp.data,end="---->")
            temp=temp.next
        print(temp.data)




o=CircularList()
num=int(input())
for i in range(num):
    x=int(input())
    o.insertatbegin(x)
o.display()