
class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        rev=st[::-1]
        if rev==st:
            return True
        else:
            return False
