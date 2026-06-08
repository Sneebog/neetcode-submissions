class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            s1 = -(heapq.heappop(maxHeap))
            s2 = -(heapq.heappop(maxHeap))
            if s1 > s2:
                heapq.heappush(maxHeap, - (s1 - s2))
        
        maxHeap.append(0)
        return -(maxHeap[0])
            