class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next
    def insert(self,head,data):
        if head == None:
            return Node(data)
        elif head.next == None:
            head.next = Node(data)
            #print(head.data)
        else:
            self.insert(head.next,data)
        print(head.data)
        return head

mylist= Solution()
inputlist = [1,2,3]
head=None
for d in inputlist:
    head=mylist.insert(head,d)
    #print(head.data)

mylist.display(head);
