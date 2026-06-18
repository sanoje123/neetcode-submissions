# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        tail = result_head

        carry = 0
        while l1 or l2:
            val1 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            
            val2 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next

            res = val1 + val2 + carry
            carry = res // 10
            res = res % 10

            tail.next = ListNode(res)
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)

        return result_head.next


            

