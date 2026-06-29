class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for one in strs:
            res=one+res
            res+=("00" + str(len(one)))[-3:]
        
        return ("00" + str(len(strs)))[-3:] + res
#002WorldHello005005
    def decode(self, s: str) -> List[str]:
        left = 3
        length = int(s[:3])
        res = [""]*length
        for i in range(length):
            lenstrindex = len(s) - i*3
            lenstr = int(s[lenstrindex-3:lenstrindex])
            res[length-i - 1] = s[left:left+lenstr]
            left+=lenstr
        return res






