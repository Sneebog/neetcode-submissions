class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_map = {}
        stack = []
        for i in range(0,len(position)):
            fleet_map[position[i]] = speed[i]

        for p, s in sorted(fleet_map.items(), reverse=True):
            stack.append(p)
            if len(stack) >= 2 and (target - stack[-2]) / fleet_map[stack[-2]] >= ((target - p) / s):
                stack.pop()

        return len(stack)

            
