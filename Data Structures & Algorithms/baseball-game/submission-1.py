class Solution:
    def calPoints(self, operations: List[str]) -> int:

        
        scores = []
        for s in operations:
            if s == "+":
                scores.append(scores[len(scores) - 2] + scores[len(scores) - 1])
            elif s=="D":
                scores.append(scores[len(scores) - 1]*2)
            elif s =="C":
                scores.pop()
            else:
                scores.append(int(s))
        return sum(scores)
