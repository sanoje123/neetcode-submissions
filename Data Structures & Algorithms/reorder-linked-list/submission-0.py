# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            pom = curr.next
            curr.next = prev
            prev = curr
            curr = pom
        
        l = head
        r = prev

        while r:
            temp_l = l.next
            l.next = r
            l = temp_l
            temp_r = r.next
            r.next = temp_l
            r = temp_r




            
            






        