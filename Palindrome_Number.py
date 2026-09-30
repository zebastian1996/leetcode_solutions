# program eget gjort utan kolla upp saker.
# man ska kolla om det är True eller False om det är samma om man vänder på siffrorna 

x = 123
x = 121
class Solution:
    def isPalindrome(self, x: int) -> bool:
        nuvarande = str(x)
        reverse = nuvarande[::-1]

        if nuvarande == reverse:
            samma = True 
        else:
            samma = False

        # print("reverse:",reverse)
        # print("nuvarande:",nuvarande)
        # print("true or false = :",samma )

        return samma

lösning = Solution()
print(lösning.isPalindrome(x))
