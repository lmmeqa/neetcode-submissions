from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        counts = [0]*numCourses
        order = []
        for req in prerequisites:
            graph[req[1]].append(req[0])
            counts[req[0]]+=1
        queue = deque()
        for coursenumber, numprereqs in enumerate(counts):
            if numprereqs == 0:
                queue.append(coursenumber)
        while queue:
            taken = queue.popleft()
            order.append(taken)
            for course in graph[taken]:
                counts[course]-=1
                if counts[course] == 0:
                    queue.append(course)
        return [] if any(counts) else order

        
            
        