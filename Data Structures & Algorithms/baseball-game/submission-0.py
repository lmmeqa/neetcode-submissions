class Solution:
    def calPoints(self, operations: List[str]) -> int:

        
        scores = []
        for s in operations:
            if s == "+":
                scores.append(int(scores[len(scores) - 2]) + int(scores[len(scores) - 1]))
            elif s=="D":
                scores.append(int(scores[len(scores) - 1])*2)
            elif s =="C":
                scores.pop()
            else:
                scores.append(int(s))
        return sum(scores)
