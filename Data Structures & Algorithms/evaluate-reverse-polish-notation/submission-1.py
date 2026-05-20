class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.startswith("-") and token[1:].isnumeric() or token.isnumeric():
                stack.append(token)
            else:
                print(stack, token)
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    calc_num = num2 + num1
                elif token == '-':
                    calc_num = num2 - num1
                elif token == '*':
                    calc_num = num2 * num1
                else:
                    calc_num = int(num2 / num1)
                stack.append(str(calc_num))
        return int(stack.pop())