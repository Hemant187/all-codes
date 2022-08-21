# Create a class node. node have data and next data pointer
class Node:
    def __init__(self ,data=None ,next=None):
        self.data = data
        self.next = next

# Create a new class name LinkedList which have all needed function
class LinkedList:
    # initialize node's head as none
    def __init__(self):
        self.head = None
    
    # Create a function for inserting list in the beginning and linked with privious one 
    def insert_at_begining(self, data):
        node = Node(data ,self.head)
        self.head = node
    
    # Create a funtion to print all list elements
    def print(self):
        itr = self.head
        llist = ''
        while itr:
            swip = ''
            if itr.next:
                swip ="-->"
            llist += str(itr.data) + swip 
            itr = itr.next
        return print(llist)

    # Create a funtion to get the lenght of linkedlist
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    # Create a function to insert and link list in the end of listnode
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    # Create a function to insert data in perticular index
    def insert_at(self, index ,data):
        if index < 0 or index > self.get_lenght():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # Create a function to remove  an item from any an index
    def remove_at(self,index):
        if index < 0 or index > self.get_lenght():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
            count += 1
            itr = itr.next

    # Create a function to add another list's item in the end of Linkedlist
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    # initialize LinkedList as l1
    l1 = LinkedList()
    l1.insert_values(['apple','banana','orange'])
    # print Linkedlist items
    l1.print()