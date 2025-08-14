#Queue : AQ is a linear data structure that follows the fifo 
# fifo = first in first out
# The first element added to the queue is the first one to be removed
# Example
# Ticket counter: The person who arrives first is served first .
#operations
#enqueue-->insertattend
#denqueue--->removeatbegin
#peek---->return head
#isempty--->self.head is None

#queue implementation
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
class Queue:
    def __init__(self):
        self.head=None
    
    def enqueue(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        elif self.head.next is None:
            top=self.head.data
            self.head=None
            return top
        else:
            top=self.head.data
            self.head=self.head.next
            return top
    
    def peek(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            return self.head.data
        
    def isEmpty(self):
        return self.head is None
    
    def display(self):
        if self.head is None:
            print("Queue is Empty")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


q=Queue()
num=int(input())
for i in range(num):
    s=input().split()
    if s[0]=="enqueue":
        q.enqueue(s[1])
    elif s[0]=="dequeue":
        q.dequeue()
    elif s[0]=="peek":
        print(q.peek())
q.display()

# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.display()
# print("\nAfter Dequeue:")
# q.dequeue()
# q.display()
# print("\nPeek value=",(q.peek()))
# print("Is empty=",q.isEmpty())
# print("After Denque:")
# q.dequeue()
# q.display()


