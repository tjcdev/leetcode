# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head and head.next:
            if str(head.val) == "T":
                return True
            head.val = "T"
            head = head.next
        return False