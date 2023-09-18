# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mapping = {}
        while head not in mapping:
            if head == None:
                return False
            mapping[head] = head.val
            head = head.next
        return True

        