
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class ReverseLinkedList:
    """
    Problem: Reverse a linked list 

    Key Insights: 

    Iterative: current.next = prev 

    Recursive: head.next.next = head, head.next = None  

    Time Complexity: 
    Iterative: O(n): Must iterate through entire list 
    Recursive: O(n): Must iterate through entire list 

    Space Complexity: 
    Iterative: O(1): Regardless of size of list, only have prev, next
    Recursive: O(n): n recursive calls on call stack 
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
        else: 
            current = self.head 
            while current.next: 
                current = current.next 
            current.next = new_node
     
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else: 
            current = self.head 
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current 
            current = next
        self.head = prev

    def reverse_recursive(self, head: Node) -> Node: 
        if not head:
            return None 

        # Track the final node 
        new_head = head 

        # At the last node, head.next = None 
        if head.next:
            # When you pop back up from the last node, you are at the 2nd to last node 
            # new_head will be the final node  
            new_head = self.reverse_recursive(head.next)
            # Set the next pointer of the next node to current node 
            head.next.next = head 
        head.next = None 
        return new_head

linked_list = LinkedList()
linked_list.append(1) 
linked_list.append(2) 
linked_list.append(3) 
linked_list.display() 
linked_list.reverse()
linked_list.display()
