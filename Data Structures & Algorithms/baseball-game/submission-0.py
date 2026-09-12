class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == '+':
                s1 = stack[-1]
                s2 = stack[-2]
                stack.append(s1+s2)
            elif op == 'D':
                s1 = stack[-1]
                stack.append(s1 * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op)) 
        return sum(stack)
