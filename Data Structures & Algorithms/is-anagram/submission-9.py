class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!= len(t)):
             return False
        seen = {}
        for i in range(0,len(s)):
            print(s[i:i+1])
            if s[i:i+1] not in seen:
                seen[s[i:i+1]] = 1
            else:
                seen[s[i:i+1]] = seen[s[i:i+1]] + 1
        for i in range(0,len(s)):
            if t[i:i+1] not in seen:
                return False
            seen[t[i:i+1]] = seen[t[i:i+1]] - 1
        for t in seen:
            if (seen[t] != 0):
                return False
        return True
        
        
        
        