class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

#the method below removes duplicates for a list in ascending order
    def removeDuplicates(self,head):
        if head == None:
            return None;
        s = head;
        while s.next != None:
            if s.data == s.next.data:
                s.next = s.next.next
            else:
                s = s.next

        return head


mylist= Solution()
head=None
T = [1,2,2,3,3,4]
for element in T:
    head=mylist.insert(head,element)
head=mylist.removeDuplicates(head)
mylist.display(head);
