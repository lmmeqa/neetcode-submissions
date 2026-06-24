class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        metaStrs = {}
        for str in strs:
            metastr = "".join(sorted(list(str)))
            if metastr in metaStrs:
                metaStrs[metastr].append(str)
            else:
                metaStrs[metastr] = [str]
        answer = []
        for metastr in metaStrs:
            answer.append(metaStrs[metastr])
        return answer
