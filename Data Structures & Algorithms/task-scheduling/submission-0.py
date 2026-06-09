class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        max_heap = [-x for x in counts.values()]
        # max_heap = [0] * 26
        # for task in tasks:
        #     idx = ord(task) - ord("A") + 1
        #     max_heap[idx] -= 1
        heapq.heapify(max_heap)

        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                val = 1 + heapq.heappop(max_heap)
                if val:
                    q.append((val, time + n))

            if q and q[0][1] == time:
                task = q.popleft()
                heapq.heappush(max_heap, task[0])
        return time