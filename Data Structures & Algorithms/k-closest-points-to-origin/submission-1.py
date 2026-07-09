import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for point in points:
            distance = (point[0]**2 + point[1]**2)
            heapq.heappush(distances, (-distance,point))
            if len(distances) > k:
                heapq.heappop(distances)
        return [point for distance,point in distances]

        