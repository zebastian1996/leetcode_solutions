class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        start = ListNode(0)
        nummer = start
        siffra = 0
 
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        start = ListNode(0)
        nummer = start
        siffra = 0
        
        while list1 is not None or list2 is not None:
            
            if list1 is None:
                siffra = list2.val 
                list2 = list2.next
            elif list2 is None:
                siffra = list1.val
                list1 = list1.next
            elif list1.val <= list2.val:
                siffra = list1.val
                list1 = list1.next
            else:
                siffra = list2.val
                list2 = list2.next

            nummer.next = ListNode(siffra)
            nummer = nummer.next
        return  start.next


lösning = Solution()
lösning.mergeTwoLists(list1,list2)


# över är min lösning med lite hjälp av en gammal övning samt lite googlande