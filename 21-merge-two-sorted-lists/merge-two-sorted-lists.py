# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list2 == None and list1 == None:
            return list1

        elif list1 == None and list2 != None:
            return list2

        elif list1 != None and list2 == None:
            return list1

        if list1.val < list2.val:
            seek, target = list1, list2
        else:
            seek, target = list2, list1

        head = seek

        # seeking is always in 'next'
        while seek and target:

            # if there is a next node in seeking list
            # and if the value of seek is smaller than target
            # do until a lower val in target is found

            while seek.next and seek.next.val < target.val:
                seek = seek.next
            # switch target and seek
            seek.next, target = target, seek.next
            # go to next seek
            seek = seek.next

        return head


        
    



