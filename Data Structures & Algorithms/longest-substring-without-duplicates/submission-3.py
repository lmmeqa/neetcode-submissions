class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        seen = set()
        maxlength = 0
        currlength = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                currlength -= 1
            else:
                seen.add(s[right])
                currlength+=1
                maxlength = max(maxlength, currlength)
        return maxlength

        