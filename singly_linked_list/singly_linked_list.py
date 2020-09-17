
class Node:

    def __init__(self, value, next_node=None):
        #value that the node is holding
        self.value = value
        #ref to the next node in the chain
        self.next_node = next_node

    def get_value(self):
        """
        method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next

class LinkedList:

    def __initt__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #wrap the value in a new node
        new_node = Node(value)
        #check if the linked list is empty
        if self.head is None and self.tail is None:
            #set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        #otherwise the list nust have at least one item in there
        else:
            #update the last node's "next_node" to the new node
            self.tail.set_next(new_node)
            #update the "self-tail" to point to th new node that we just added
            self.tail = new_node

    def remove_tail(self):
        """
        remove the last node in teh chain and return its Value
        """
        #check for empty LinkedList
        if self.head is None and self.tail is None:
            #return None
            return None
        #check if there is only one node
        if self.head ==self.tail:
            #store the value of the node that we aere going to remove
            value = self.tail.get_value()
            #remove the node
            #set head to the tail to None
            self.head = None
            self.tail = None
            #return the stored value
            return value
        #otherwise
        else:
            #store the value of the node tat we are going to remove
            value.self.tail.get_value()
            #we need to set  the "self.tail" to the second to last nodes
            #we can only do this by traversing the whole list from beginning to new_node

            #starting from the remove_head
            current_node = self.head

            #keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                #keep looping
                current_node = current_node.get_next()

            #at the end of the iteration set "self.tail" to the current_node
            self.tail = current_node
            #set the new tail's "next_node" to None
            self.tail.set_next(None)
            #return Value
            return value

    def remove_head(self):
        #check for empty list
        if self.head is None and self.tail is None:
            #return None
            return None
        if self.head == sail.tail:
            #store the value of the node that we are going to remove
            value =self.head.get_value()
            #remove teh node
            #set the head and the tail to None
            self.head = None
            self.tail = None
            #return the stored Value
            return value
        else:
            #store the old head's Value
            value = self.head.get_value()
            #set self.head to old head's next
            self.head = self.head.get_next()
            #return the Value
            return value


n1 = Node(1)
n1 = Node(2)
n1 = Node(3)
n1 = Node(4)

print(n1.set_next(2))
print(n1.get_value())
