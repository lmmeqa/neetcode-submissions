from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        counts = [0]*numCourses
        for course,prereq in prerequisites:
            prereqs[prereq].add(course)
            counts[course]+=1
        queue = deque()
        for index, count in enumerate(counts):
            if count == 0:
                queue.append(index)
        count = 0
        while queue:
            takenCourse = queue.popleft()
            count+=1
            for course in prereqs[takenCourse]:
                counts[course]-=1
                if counts[course] == 0:
                    queue.append(course)
        return count==numCourses

        
        
                
      
            
        
            



        