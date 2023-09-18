# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mapping = set()
        while head not in mapping:
            if head == None:
                return False
            mapping.add(head)
            head = head.next
        return True

        