class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hashmap = {}
        freq_nums = []
        for num in nums:
            num_hashmap[num] = num_hashmap.get(num, 0) + 1
        
        for num, count in (num_hashmap.items()):
            freq_nums.append((count, num ))
        freq_nums.sort()

        ans = []
        while len(ans) < k:
            ans.append(freq_nums.pop()[1])

        return ans