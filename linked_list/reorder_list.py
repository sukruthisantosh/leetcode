# Definition for singly-linked list.
from operator import length_hint
from typing import Optional

from binary_search.binary_search import solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2







# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# l0 -> ln -> l1 -> ln-1 -> l2

solution = Solution()

five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

print(solution.reorderList(head=one))