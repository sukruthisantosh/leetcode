from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temporary = current.next
            current.next = prev
            prev = current
            current = temporary
        return prev


solution = Solution()
five = ListNode(5,None)
four = ListNode(4,five)
three = ListNode(3,four)
two = ListNode(2,three)
one = ListNode(1,two)

print(solution.reverseList(head=one))