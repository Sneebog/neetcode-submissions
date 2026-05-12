class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for key, value in counter.items():
            freq[value].append(key)

        output = []
        count = len(freq) - 1
        while k > 0:
            if len(freq[count]) > 0:
                output.append(freq[count].pop())
                k -= 1
            else:
                count -= 1
        print(counter)
        return output