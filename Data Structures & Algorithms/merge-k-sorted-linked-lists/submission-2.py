# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            p1 = l1
            p2 = l2
            dummy = ListNode()
            tail = dummy
            while p1 and p2:
                if p1.val < p2.val:
                    tail.next = p1
                    tail = tail.next
                    p1 = p1.next
                else:
                    tail.next = p2
                    tail = tail.next
                    p2 = p2.next
            while p1:
                tail.next = p1
                p1 = p1.next
                tail = tail.next
            while p2:
                tail.next = p2
                p2 = p2.next
                tail = tail.next
            return dummy.next



        if not lists:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(merge(l1, l2))
            lists = mergedList
        return lists[0]
        