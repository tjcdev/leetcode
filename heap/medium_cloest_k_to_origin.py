class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            dist = (x ** 2 + y ** 2)
            heapq.heappush(max_heap,(-dist,[x,y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        for item in max_heap:
            dist,point = item
            res.append(point)
        return res