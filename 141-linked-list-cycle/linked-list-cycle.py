# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #mapping = set()
        #while head not in mapping:
        #    if head == None:
        #       return False
        #    mapping.add(head)
        #    head = head.next
        #return True

    # "hare and tortoise" algorithm
        fast_pointer = head
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                return True
        return False