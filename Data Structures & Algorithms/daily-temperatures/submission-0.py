class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack for getting temps
        hot_stack = []
        # used to store temps and their indexes
        temp_map = {}
        # for final days result
        result = [0]  * len(temperatures)


        # Loop through temperatures
        for i in range(0, len(temperatures)):
            #get current temp
            temp = temperatures[i]
            #while stack exists and the top element is less then the current temp pop
            # print(temp, hot_stack, temp_map)
            while hot_stack and hot_stack[-1] < temp:
                    val = hot_stack.pop()
                    index = temp_map[val].pop()
                    result[index] = i - index
            
            hot_stack.append(temp)
            temp_map.setdefault(temp, []).append(i)

        return result

