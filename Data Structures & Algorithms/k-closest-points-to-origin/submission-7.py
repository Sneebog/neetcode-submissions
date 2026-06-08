class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_heap = []
        heapq.heapify(res_heap)
        for i in range(0, len(points)):
            distance = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            print(points[i], distance)
            heapq.heappush(res_heap, (-distance, i))
            if len(res_heap) > k:
                heapq.heappop(res_heap)
        res = []
        for i in range(0, len(res_heap)):
            point = heapq.heappop(res_heap)
            res.append(points[point[1]])
        return res
        



