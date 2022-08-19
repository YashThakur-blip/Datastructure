from typing import List


class Node(object):

    def __init__(self, data, next=None):
        self.data =  data
        self.next = next

class linkedlist(object):

    def __init__(self):
        self.head = None

    def InsertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def printlist(self):
        temp = self.head
        while(temp):
            print(f'{temp.data} ->' , end="")
            temp = temp.next
            # print("NULL")
        
#drivers code

List = linkedlist()
List.InsertAtStart(15)
List.InsertAtStart(10)
List.InsertAtStart(11)
List.InsertAtStart(21)

List.printlist()