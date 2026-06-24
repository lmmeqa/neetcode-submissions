from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tree = defaultdict(list)
        numprereqs = [0]*numCourses
        for prereq in prerequisites:
            tree[prereq[1]].append(prereq[0])
            numprereqs[prereq[0]] += 1
        queue = deque()
        for course, pending in enumerate(numprereqs):
            if pending == 0:
                queue.append(course)
        while queue:
            taken = queue.popleft()
            for course in tree[taken]:
                numprereqs[course]-=1
                if numprereqs[course] == 0: queue.append(course)
        return not any(numprereqs)


        



        