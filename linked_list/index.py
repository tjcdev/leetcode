class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    def insertNode(self, val, pos):
        target = Node(val)
        if (pos == 0):
            target.next = self.head
            self.head = target
            return
        def getPrev(pos):
            temp = self.head
            count = 1
            while(count < pos):
                temp = temp.next
                count += 1
            return temp
        prev = getPrev(pos)
        nextNode = prev.next
        target.next = nextNode
        prev.next = target

    def deleteNode(self, key):
        temp = self.head
        if(temp is None):
            return
        if(temp.data == key):
            self.head = temp.next
            temp = None
        while(temp.next.data is key):
            temp = temp.next
        
        target_node = temp.next
        temp.next = target_node.next
        target_node.next = None 

linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()

linked_list.insertNode(2, 2)

linked_list.printList()


# NOTE THAT THIS DOES NOT WORK
# ERROR
linked_list.deleteNode(1)

linked_list.printList()