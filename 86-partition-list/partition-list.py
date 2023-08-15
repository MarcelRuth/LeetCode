# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left = []
        right = []

        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next

        # starts linked list
        dummy_start_node = ListNode(None)
        current_node = dummy_start_node

        for x in left:
            current_node.next   = ListNode(x) # makes a ListNode at each next node (linking list)
            current_node        = current_node.next
        for x in right:
            current_node.next   = ListNode(x) # vide supra
            current_node        = current_node.next

        return dummy_start_node.next

