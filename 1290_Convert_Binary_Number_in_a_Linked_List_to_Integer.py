class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num


val1 = ListNode(1)
val2 = ListNode(0)
val3 = ListNode(1)
val4 = ListNode(1)
val1.next = val2
val2.next = val3
val3.next = val4

sol = Solution()
print(sol.getDecimalValue(val1))
