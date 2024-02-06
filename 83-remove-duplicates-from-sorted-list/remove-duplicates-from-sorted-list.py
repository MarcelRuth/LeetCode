from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:  # Check if the input list is empty
            return None
        
        is_in = set()  # Using set for faster lookups
        dummy = ListNode(0)  # Dummy node to handle edge cases more easily
        new_list = dummy  # Pointer to build the new list without duplicates
        
        while head:
            if head.val not in is_in:
                is_in.add(head.val)
                new_list.next = ListNode(head.val)  # Create a new node for unique values
                new_list = new_list.next  # Move the pointer forward
            head = head.next  # Move to the next node in the input list
        
        return dummy.next  # Return the next of dummy to skip the initial dummy node
