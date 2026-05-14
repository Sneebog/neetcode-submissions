class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        for i in range(0, len(numbers)):
            pointer = len(numbers) -1
            if target - numbers[i] in num_set:
                while target - numbers[i] != numbers[pointer]:
                    pointer -= 1
                if i != pointer:
                    return [i + 1, pointer + 1]
