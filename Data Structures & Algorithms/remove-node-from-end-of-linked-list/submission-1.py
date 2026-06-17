# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # # my soution
        # def removeElAtIndexI(head: Optional[ListNode], i: int) -> Optional[ListNode]:
        #     # delete element at index n
        #     count = 0
        #     temp = head
        #     prev = None
        #     while temp:
        #         if count == i:
        #             if not prev:
        #                 head = head.next
        #                 break

        #             prev.next = temp.next
        #             break   
        #         count += 1
        #         prev = temp
        #         temp = temp.next

        #     return head

        # counter = 0
        # temp = head
        # while temp:
        #     counter += 1
        #     temp = temp.next
        
        # i = counter - n
        # print(i)
        # return removeElAtIndexI(head, i)

        # Their solution

        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next



        