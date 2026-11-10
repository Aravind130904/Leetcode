class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p=""

        for ch in s:
            if ch.isalnum():
                p+=ch.lower()
        return p==p[::-1]