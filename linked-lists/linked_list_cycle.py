from typing import Optional 

class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None 

class LinkedListCycle:
    """
    Problem: Linked List Cycle 

    Description: Detect if there is a cycle in the linked list 

    Key Insights: 
    1. Floyd's detection algorithm (Robert W. Floyd, 1960)
        a. slow pointer: move by 1 node, fast pointer, move by 2 nodes 
        b. If slow and fast pointers meet, there is a cycle   

    Time Complexity: O(n) time bc iterate through all the nodes 
    Space Complexity: O(1) space bc no matter how big the list, only have slow and fast pointers 
    """

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False 

        slow, fast = head, head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 

        return False
