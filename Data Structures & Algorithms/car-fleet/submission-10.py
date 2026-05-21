class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(((position[i], speed[i]) for i in range(0, len(position))), reverse = True )
        stack = []
        for i in range(0, len(cars)):
            stack.append(cars[i])
            if len(stack) >= 2 and (target - stack[-2][0]) / stack[-2][1] >= (target - cars[i][0]) / cars[i][1]:
                stack.pop()
            
            # print(stack, cars[i])

        return len(stack)