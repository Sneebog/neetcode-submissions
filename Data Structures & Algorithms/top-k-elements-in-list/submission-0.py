class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hashmap = {}
        freq_nums = []
        for num in nums:
            num_hashmap[num] = num_hashmap.get(num, 0) + 1
        
        while k > 0: 
            max_num = max(num_hashmap, key=num_hashmap.get)
            freq_nums.append(max_num)
            del num_hashmap[max_num]
            k -= 1

        return freq_nums