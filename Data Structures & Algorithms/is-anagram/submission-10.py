class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        quants = [0]*26
        for char in s:
            quants[ord(char) - ord('a')] += 1
        for char in t:
            quants[ord(char) - ord('a')] -= 1
        return not any(quants) 
        