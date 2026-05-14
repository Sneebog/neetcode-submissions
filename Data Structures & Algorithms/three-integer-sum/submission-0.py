class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = set(nums)
        answer_set= set()
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                k = len(nums) -1
                if  (0 - nums[i] - nums[j]) in num_set and i != j:
                    while nums[k] + nums[i] + nums[j] != 0 and k!= i and k != j:
                        k -= 1
                    if k != i and k != j:
                        triplet = [nums[k], nums[i], nums[j]]
                        triplet.sort()
                        str_triplet = str(triplet[0]) + ' '  + str(triplet[1]) + ' ' + str(triplet[2])
                        if str_triplet not in answer_set:
                            answer_set.add(str_triplet)
            
        answer_array = []
        for val in answer_set:
            arr = list(map(int, val.split()))

            answer_array.append(arr)

        return answer_array