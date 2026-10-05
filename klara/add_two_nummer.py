


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        start = ListNode(0)
        sista = start
        vidare = 0

        while l1 is not None or l2 is not None or vidare != 0:
            tal1 = 0
            tal2 = 0

            if l1 is not None:
                tal1 = l1.val
                l1 = l1.next

            if l2 is not None:
                tal2 = l2.val
                l2 = l2.next

            summa = tal1 + tal2 + vidare
            siffra = summa % 10
            vidare = summa // 10

            sista.next = ListNode(siffra)
            sista = sista.next

        return start.next

lösning = Solution()
lösning.addTwoNumbers(l1, l2)

