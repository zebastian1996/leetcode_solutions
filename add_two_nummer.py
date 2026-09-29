class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

first = []



class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        vidare = 0
        while l1 is not None:
            

            if l1.val+l2.val < 10:
                first.append(l1.val + l2.val + vidare)
                print("1")
            elif vidare <= 1:
                first.append((l1.val + l2.val) % 10)
                vidare = ((l1.val + l2.val) // 10) 
                print("2")
            else:
                vidare = ((l1.val + l2.val) // 10)
                first.append((l1.val + l2.val) % 10) 
                print("3")
            l1 = l1.next    
            l2 = l2.next
        result = int("".join(map(str, first)))

        print(result)

lösning = Solution()
lösning.addTwoNumbers(l1, l2)


