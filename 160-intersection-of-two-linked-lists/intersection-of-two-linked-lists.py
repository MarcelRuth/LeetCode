# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:


        first_set = set()
        current = headA

        # save the first linked list in set 
        while current:
            first_set.add(current)
            current = current.next

        current = headB

        # check if same tail is found in first_set
        while current:
            if current in first_set:
                return current
            current = current.next

        return None
            
        