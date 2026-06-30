class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalindrome(sub:str):
            left,right = 0, len(sub) - 1
            while left<right:
                if sub[left]!= sub[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True
        count = 0
        for left in range(len(s)):
            for right in range(left + 1, len(s)+1):
                if ispalindrome(s[left:right]):
                    count+=1
        return count



