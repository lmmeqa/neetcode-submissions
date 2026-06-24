class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        lettercounts = [0]*26
        maxCount = 0
        for right in range(len(s)):
            lettercounts[ord(s[right]) - ord('A')]+=1
            while right-left + 1-k > max(lettercounts):
                lettercounts[ord(s[left]) - ord('A')]-=1
                left+=1
            maxCount = max(maxCount, sum(lettercounts))
        return maxCount



        
        