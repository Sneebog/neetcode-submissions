class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        l = 0
        r = len(numbers) - 1
        while l < r:
            diff = numbers[l] + numbers[r]
            if diff == target:
                return [l + 1, r + 1]
            elif diff > target:
                r -= 1
            else:
                l += 1
        return []