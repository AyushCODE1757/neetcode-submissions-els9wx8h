# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            if not head:
                return None
            newHead = head
            if head.next:
                newHead = reverse(head.next)
                head.next.next = head
            head.next = None
            return newHead
        # First find half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        first = head
        second = reverse(second)
        while(second):
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
