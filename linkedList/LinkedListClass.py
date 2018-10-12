#Linked list consists of a head node which is the first node of the list.
#Each node has two parameters, data and a pointer which points to the next node in the list
class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    #This method returns the stored data
    def get_data(self):
        return self.data

    #This method returns the next node (the node to which the object node points)
    def get_next(self):
        return self.next_node

    #This method resets the pointer to a new node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insert_onto_tail(self, data):
        new_node = Node(data)
        self.tail.set_next(new_node)  #This makes the pointer point towards self.head ie. our previous head ????
        self.tail = new_node

    def insert_onto_head(self, data):
        new_node = Node(data)  #This instantianates the class Node with some value data
        new_node.set_next(self.head)  #This makes the pointer point towards self.head ie. our previous head ????
        self.head = new_node  #Sets the head to this new node.

    #Finds the size of linked list
    def size(self):
        current = self.head
        count = 0
        while current: #Once we get to end of linked list current = None and we will break out the loop
            count = count + 1
            current = current.get_next()
        return count

    #This method searches for a node with particular data. Returns an error if not found
    def search(self, data):
        current = self.head
        found = False
        while current and found == False: # 'current' and 'found == False' seperate things
            if current.get_data == data:
                found = True
            else:
                current = current.get_next()
        if current == None:  #If we get to the end of the list current.get_next will give None as no next node.
            raise ValueError("Data not in the list")
        return current


    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in the list")
        if previous == None: #ie if the while loop was completed asap due to found=True
            self.head = current.get_next() #So we want to delete the head so just set head to next node!
        else:
            previous.set_next(current.get_next)

    def display(self):
        current = self.head
        while current: #ie while current == True or while current != None
            #print(current)  #this would print a node object - self.head = new_node in insert function which is a node
            print(current.get_data()) #this will print the actual value
            current = current.get_next()

node = Node(6, Node(5))   #Node(5) is the pointer, so effectively we now have two nodes
print(node.get_data())
print(node.get_next().get_data()) #node.get_next() gives Node(5) so to print the value we use the .get_data()
node2 = Node(3)
mylist = LinkedList(node2, node2)
mylist.insert_onto_tail(5)
mylist.insert_onto_tail(7)
mylist.insert_onto_tail(9)
mylist.insert_onto_tail(11)
mylist.insert_onto_head(13)
mylist.display()
